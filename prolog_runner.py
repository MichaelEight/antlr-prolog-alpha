import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox, filedialog
import networkx as nx
import matplotlib.pyplot as plt
from MiniPrologVisitor import MiniPrologVisitor
import itertools

RETURN_KEY = "<Return>"

class PrologInterpreter(MiniPrologVisitor):
    def __init__(self):
        self.facts = {}  # { predicate: set of tuples }
        self.rules = []  # list of (head_pred, head_args, body_atoms)

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitFact(self, ctx):
        atom = ctx.atom()
        pred, args = self._parse_atom(atom)
        self.facts.setdefault(pred, set()).add(tuple(args))

    def visitRule(self, ctx):
        head_pred, head_args = self._parse_atom(ctx.atom())
        body_atoms = []
        for atom_ctx in ctx.atomList().atom():
            pred, args = self._parse_atom(atom_ctx)
            body_atoms.append((pred, args))
        self.rules.append((head_pred, head_args, body_atoms))

    def visitQuery(self, ctx):
        for atom in ctx.atomList().atom():
            pred, args = self._parse_atom(atom)
            query_str = f"{pred}({', '.join(args)})"
            print(f"{query_str}:")

            results = self._match_fact(pred, args)
            if not results:
                results = self._match_rules(pred, args)

            if results:
                printed = False
                for binding in results:
                    if binding:
                        print("   " + ", ".join(f"{k} = {v}" for k, v in binding.items()))
                        printed = True
                    else:
                        print("   ✅ TRUE")
                        printed = True
                if not printed:
                    print("   ✅ TRUE")
            else:
                print("   ❌ No match")

    def _match_fact(self, pred, args):
        results = []
        if pred not in self.facts:
            return results

        for fact_args in self.facts[pred]:
            bindings = {}
            match = True
            for q, f in zip(args, fact_args):
                if q[0].isupper():
                    if q in bindings:
                        if bindings[q] != f:
                            match = False
                            break
                    else:
                        bindings[q] = f
                elif q != f:
                    match = False
                    break
            if match:
                results.append(bindings)
        return results

    def _match_rules(self, pred, args):
        matches = []
        for head_pred, head_args, body_atoms in self.rules:
            if head_pred != pred or len(head_args) != len(args):
                continue

            var_map = {}  # Map rule vars to query args
            consistent = True
            for h_arg, q_arg in zip(head_args, args):
                if h_arg[0].isupper():
                    var_map[h_arg] = q_arg
                elif h_arg != q_arg:
                    consistent = False
                    break

            if not consistent:
                continue

            all_bindings = [{}]
            for b_pred, b_args in body_atoms:
                new_results = []
                for binding in all_bindings:
                    applied_args = [
                        binding.get(var_map.get(a, a), var_map.get(a, a))
                        if a[0].isupper() else a
                        for a in b_args
                    ]
                    sub_results = self._match_fact(b_pred, applied_args)
                    for sub in sub_results:
                        combined = binding.copy()
                        combined.update(sub)
                        new_results.append(combined)
                all_bindings = new_results

            for b in all_bindings:
                final_binding = {}
                for var in args:
                    if var[0].isupper():
                        final_binding[var] = b.get(var_map.get(var, var), var_map.get(var, var))
                matches.append(final_binding)
        return matches

    def _parse_atom(self, atom_ctx):
        pred = atom_ctx.ID().getText()
        args = [t.getText() for t in atom_ctx.args().term()]
        return pred, args


class PrologGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini Prolog Interpreter")
        self.geometry("800x600")

        # --- Menu Bar for File operations ---
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_to_file)
        filemenu.add_command(label="Load", accelerator="Ctrl+L", command=self.load_from_file)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)
        # Keyboard shortcuts for menu actions
        self.bind('<Control-s>', lambda e: self.save_to_file())
        self.bind('<Control-l>', lambda e: self.load_from_file())

        # --- View menu for Graph visualization ---
        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Graph", accelerator="G", command=self.visualize_graph)
        menubar.add_cascade(label="View", menu=viewmenu)
        # Keyboard shortcut for graph
        self.bind('<Key-g>', lambda e: self.visualize_graph())

        self.interpreter = PrologInterpreter()

        top_frame = tk.Frame(self)
        top_frame.pack(fill=tk.X, padx=5, pady=5)

        # Facts panel
        self.fact_frame = tk.LabelFrame(top_frame, text="Facts")
        self.fact_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.fact_entry = tk.Entry(self.fact_frame)
        self.fact_entry.pack(fill=tk.X, padx=5, pady=5)
        self.fact_entry.bind(RETURN_KEY, lambda e: self.add_fact())
        tk.Button(self.fact_frame, text="Add Fact", command=self.add_fact).pack(padx=5, pady=5)
        self.fact_list = tk.Listbox(self.fact_frame)
        self.fact_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        fact_btn_frame = tk.Frame(self.fact_frame)
        fact_btn_frame.pack(fill=tk.X, pady=5)
        tk.Button(fact_btn_frame, text="Edit Fact", command=self.edit_fact).pack(side=tk.LEFT, expand=True, padx=5)
        tk.Button(fact_btn_frame, text="Delete Fact", command=self.delete_fact).pack(side=tk.LEFT, expand=True, padx=5)

        # Rules panel
        self.rule_frame = tk.LabelFrame(top_frame, text="Rules")
        self.rule_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.rule_entry = tk.Entry(self.rule_frame)
        self.rule_entry.pack(fill=tk.X, padx=5, pady=5)
        self.rule_entry.bind(RETURN_KEY, lambda e: self.add_rule())
        tk.Button(self.rule_frame, text="Add Rule", command=self.add_rule).pack(padx=5, pady=5)
        self.rule_list = tk.Listbox(self.rule_frame)
        self.rule_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        rule_btn_frame = tk.Frame(self.rule_frame)
        rule_btn_frame.pack(fill=tk.X, pady=5)
        tk.Button(rule_btn_frame, text="Edit Rule", command=self.edit_rule).pack(side=tk.LEFT, expand=True, padx=5)
        tk.Button(rule_btn_frame, text="Delete Rule", command=self.delete_rule).pack(side=tk.LEFT, expand=True, padx=5)

        # Query panel
        self.query_frame = tk.LabelFrame(self, text="Query")
        self.query_frame.pack(fill=tk.X, padx=5, pady=5)
        self.query_entry = tk.Entry(self.query_frame)
        self.query_entry.pack(fill=tk.X, padx=5, pady=5)
        self.query_entry.bind(RETURN_KEY, lambda e: self.ask_query())
        tk.Button(self.query_frame, text="Ask", command=self.ask_query).pack(pady=5)

        # History panel
        history_frame = tk.LabelFrame(self, text="History")
        history_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.history = scrolledtext.ScrolledText(history_frame, state='disabled')
        self.history.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initialize command history, panel selection, and mode
        self.query_history = []
        self.history_index = 0
        self.selected_panel = None
        self.mode = 'select'  # modes: 'select', 'input', 'none'
        self.select_panel('fact')
        # Entry focus sets input mode
        self.fact_entry.bind('<FocusIn>', lambda e: setattr(self, 'mode', 'input'))
        self.rule_entry.bind('<FocusIn>', lambda e: setattr(self, 'mode', 'input'))
        self.query_entry.bind('<FocusIn>', lambda e: setattr(self, 'mode', 'input'))
        # Bind arrow keys for query history
        self.query_entry.bind('<Up>', self.prev_query)
        self.query_entry.bind('<Down>', self.next_query)
        # Double-click to edit in listboxes
        self.fact_list.bind('<Double-1>', lambda e: self.edit_fact())
        self.rule_list.bind('<Double-1>', lambda e: self.edit_rule())
        # Global key bindings for panel shortcuts and commands
        self.bind_all('<Key>', self.on_key_press)

        # Save/Load buttons
        action_frame = tk.Frame(self)
        action_frame.pack(fill=tk.X, padx=5, pady=5)
        tk.Button(action_frame, text="Save to file", command=self.save_to_file).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Load from file", command=self.load_from_file).pack(side=tk.LEFT, padx=5)

    def _parse_fact_text(self, text):
        # Validate fact syntax: predicate(arg1, arg2, ...)
        if '(' not in text or not text.endswith(')'):
            raise ValueError("Fact must be in form predicate(arg1, arg2, ...)")
        pred, args_str = text.split('(', 1)
        args_str = args_str.rstrip(')')
        if not pred.strip() or not args_str:
            raise ValueError("Fact must be in form predicate(arg1, arg2, ...)")
        args = [a.strip() for a in args_str.split(',')]
        if any(not a for a in args):
            raise ValueError("Empty argument in fact")
        return pred.strip(), args

    def add_fact(self):
        raw = self.fact_entry.get().strip()
        if not raw:
            return
        # batch split on periods
        parts = [p.strip() for p in raw.split('.') if p.strip()]
        for text in parts:
            try:
                pred, args = self._parse_fact_text(text)
            except Exception as e:
                messagebox.showerror("Invalid Fact", str(e))
                continue
            self.interpreter.facts.setdefault(pred, set()).add(tuple(args))
            self.fact_list.insert(tk.END, text + '.')
        self.fact_entry.delete(0, tk.END)

    def _parse_rule_text(self, text):
        # Splits head and body, then safely splits body atoms ignoring commas inside parentheses
        head_str, body_str = text.split(':-', 1)
        hpred, hargs_str = head_str.strip().split('(', 1)
        hargs = [a.strip() for a in hargs_str.rstrip(')').split(',')]
        # split body_str into atom texts
        atoms = []
        buf = ''
        depth = 0
        for ch in body_str:
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            if ch == ',' and depth == 0:
                atoms.append(buf.strip())
                buf = ''
            else:
                buf += ch
        if buf.strip():
            atoms.append(buf.strip())
        # parse each atom
        body_atoms = []
        for atom in atoms:
            p, a_str = atom.split('(', 1)
            args = [x.strip() for x in a_str.rstrip(')').split(',')]
            body_atoms.append((p.strip(), args))
        return hpred.strip(), hargs, body_atoms

    def add_rule(self):
        raw = self.rule_entry.get().strip()
        if not raw:
            return
        parts = [p.strip() for p in raw.split('.') if p.strip()]
        for text in parts:
            try:
                hpred, hargs, body_atoms = self._parse_rule_text(text)
            except Exception:
                messagebox.showerror("Invalid Rule", f"Invalid rule: {text}. Correct form: head(...) :- body(...) .")
                continue
            self.interpreter.rules.append((hpred, hargs, body_atoms))
            self.rule_list.insert(tk.END, text + '.')
        self.rule_entry.delete(0, tk.END)

    def edit_fact(self):
        sel = self.fact_list.curselection()
        if not sel:
            return
        idx = sel[0]
        old = self.fact_list.get(idx).rstrip('.')
        new = simpledialog.askstring("Edit Fact", "Modify fact (e.g. parent(john, mary)):", initialvalue=old)
        if not new:
            return
        text = new.strip().rstrip('.')
        # remove old
        try:
            pred, args_str = old.split('(', 1)
            args = [a.strip() for a in args_str.rstrip(')').split(',')]
            self.interpreter.facts[pred].remove(tuple(args))
            if not self.interpreter.facts[pred]:
                del self.interpreter.facts[pred]
        except Exception:
            pass
        # add new
        pred, args_str = text.split('(', 1)
        args = [a.strip() for a in args_str.rstrip(')').split(',')]
        self.interpreter.facts.setdefault(pred, set()).add(tuple(args))
        self.fact_list.delete(idx)
        self.fact_list.insert(idx, text + '.')

    def delete_fact(self):
        sel = self.fact_list.curselection()
        if not sel:
            return
        idx = sel[0]
        fact = self.fact_list.get(idx).rstrip('.')
        if not messagebox.askyesno("Delete Fact", f"Delete fact '{fact}'?"):
            return
        try:
            pred, args_str = fact.split('(', 1)
            args = [a.strip() for a in args_str.rstrip(')').split(',')]
            self.interpreter.facts[pred].remove(tuple(args))
            if not self.interpreter.facts[pred]:
                del self.interpreter.facts[pred]
        except Exception:
            pass
        self.fact_list.delete(idx)

    def edit_rule(self):
        sel = self.rule_list.curselection()
        if not sel:
            return
        idx = sel[0]
        old_text = self.rule_list.get(idx).rstrip('.')
        # Parse existing rule
        try:
            old_pred, old_args, old_body = self._parse_rule_text(old_text)
        except Exception:
            messagebox.showerror("Error", f"Stored rule '{old_text}' is invalid and cannot be edited.")
            return
        new_text = simpledialog.askstring(
            "Edit Rule",
            "Modify rule (e.g. grandparent(X, Y) :- parent(X, Z), parent(Z, Y)):",
            initialvalue=old_text
        )
        if not new_text:
            return
        new_text = new_text.strip().rstrip('.')
        # Remove old
        try:
            self.interpreter.rules.remove((old_pred, old_args, old_body))
        except ValueError:
            messagebox.showwarning("Warning", f"Original rule '{old_text}' not found in interpreter.")
        # Parse new
        try:
            new_pred, new_args, new_body = self._parse_rule_text(new_text)
        except Exception as e:
            messagebox.showerror("Invalid Rule", str(e))
            # reinstate old if removal succeeded
            self.interpreter.rules.append((old_pred, old_args, old_body))
            return
        # Add new
        self.interpreter.rules.append((new_pred, new_args, new_body))
        self.rule_list.delete(idx)
        self.rule_list.insert(idx, new_text + '.')

    def delete_rule(self):
        sel = self.rule_list.curselection()
        if not sel:
            return
        idx = sel[0]
        text = self.rule_list.get(idx).rstrip('.')
        if not messagebox.askyesno("Delete Rule", f"Delete rule '{text}'?"):
            return
        # Parse and remove
        try:
            pred, args, body = self._parse_rule_text(text)
            self.interpreter.rules.remove((pred, args, body))
        except Exception:
            messagebox.showwarning("Warning", f"Could not remove rule '{text}'. It may have been modified already.")
        self.rule_list.delete(idx)

    def ask_query(self):
        raw = self.query_entry.get().strip()
        if not raw:
            return
        # split into individual queries by period
        parts = [p.strip().rstrip('?.') for p in raw.split('.') if p.strip()]
        for text in parts:
            # record history
            self.query_history.append(text)
            self.history_index = len(self.query_history)
            # validate syntax
            try:
                if '(' not in text or not text.endswith(')'):
                    raise ValueError
                pred, args_str = text.split('(', 1)
                args = [a.strip() for a in args_str.rstrip(')').split(',')]
                if not pred.strip() or any(not a for a in args):
                    raise ValueError
            except Exception:
                messagebox.showerror("Invalid Query", "Query must be in form predicate(arg1, arg2, ...)")
                continue
            # perform query
            results = self.interpreter._match_fact(pred, args) or self.interpreter._match_rules(pred, args)
            # display
            self.history.config(state='normal')
            self.history.insert(tk.END, f"Q: {text}\n")
            if results:
                for bind in results:
                    if bind:
                        self.history.insert(tk.END, "A: " + ", ".join(f"{k} = {v}" for k, v in bind.items()) + "\n")
                    else:
                        self.history.insert(tk.END, "A: ✅ TRUE\n")
            else:
                self.history.insert(tk.END, "A: ❌ No match\n")
            self.history.insert(tk.END, "\n")
            self.history.config(state='disabled')
        # scroll to bottom and reset input
        self.history.yview(tk.END)
        self.query_entry.delete(0, tk.END)
        self.query_entry.focus_set()

    def prev_query(self, event):
        if not self.query_history:
            return 'break'
        self.history_index = max(0, self.history_index - 1)
        cmd = self.query_history[self.history_index]
        self.query_entry.delete(0, tk.END)
        self.query_entry.insert(0, cmd)
        return 'break'

    def next_query(self, event):
        if not self.query_history:
            return 'break'
        if self.history_index < len(self.query_history) - 1:
            self.history_index += 1
            cmd = self.query_history[self.history_index]
        else:
            self.history_index = len(self.query_history)
            cmd = ''
        self.query_entry.delete(0, tk.END)
        self.query_entry.insert(0, cmd)
        return 'break'

    def select_panel(self, panel):
        # Visual highlight of selected panel and focus
        self.selected_panel = panel
        for name, frame in [('fact', self.fact_frame), ('rule', self.rule_frame), ('query', self.query_frame)]:
            if name == panel:
                frame.config(highlightthickness=2, highlightbackground='blue')
            else:
                frame.config(highlightthickness=0)
        # Focus appropriate widget for navigation
        if panel == 'fact':
            self.fact_list.focus_set()
        elif panel == 'rule':
            self.rule_list.focus_set()
        else:
            self.query_entry.focus_set()

    def clear_panel_selection(self):
        # Clear visual highlight of selected panel
        self.selected_panel = None
        for _, frame in [('fact', self.fact_frame), ('rule', self.rule_frame), ('query', self.query_frame)]:
            frame.config(highlightthickness=0)

    def on_key_press(self, event):
        key = event.keysym.lower()
        # Global ESC key behavior
        if key == 'escape':
            if self.mode == 'input':
                # leave input, back to panel selection
                self.mode = 'select'
                self.focus_set()
            elif self.mode == 'select':
                # clear selection mode
                self.mode = 'none'
                self.clear_panel_selection()
                self.focus_set()
            else:
                # already none, just defocus
                self.focus_set()
            return 'break'
        # Ignore shortcuts while typing (input mode)
        if self.mode == 'input':
            return 'break'
        # Save/Load shortcuts
        if key == 's':
            self.save_to_file()
            return 'break'
        if key == 'l':
            self.load_from_file()
            return 'break'
        # Panel selection
        if key == 'f':
            self.mode = 'select'
            self.select_panel('fact')
            return 'break'
        if key == 'r':
            self.mode = 'select'
            self.select_panel('rule')
            return 'break'
        if key == 'q':
            self.mode = 'select'
            self.select_panel('query')
            return 'break'
        # Panel actions
        if key == 'a':
            if self.selected_panel == 'fact':
                self.fact_entry.focus_set()
            elif self.selected_panel == 'rule':
                self.rule_entry.focus_set()
            elif self.selected_panel == 'query':
                self.query_entry.focus_set()
            return 'break'
        if key == 'e':
            if self.selected_panel == 'fact':
                self.edit_fact()
            elif self.selected_panel == 'rule':
                self.edit_rule()
            return 'break'
        if key == 'd':
            if self.selected_panel == 'fact':
                self.delete_fact()
            elif self.selected_panel == 'rule':
                self.delete_rule()
            return 'break'
        # Other keys: default behavior

    def save_to_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".xd", filetypes=[("XD files","*.xd"),("All files","*.*")])
        if not path:
            return
        try:
            lines = []
            for pred, facts in self.interpreter.facts.items():
                for args in facts:
                    lines.append(f"{pred}({', '.join(args)}).")
            for hpred, hargs, body in self.interpreter.rules:
                body_str = ", ".join(f"{p}({', '.join(a)})" for p, a in body)
                lines.append(f"{hpred}({', '.join(hargs)}) :- {body_str}.")
            with open(path, 'w') as f:
                f.write("\n".join(lines))
        except Exception as e:
            messagebox.showerror("Save Error", str(e))

    def load_from_file(self):
        path = filedialog.askopenfilename(defaultextension=".xd", filetypes=[("XD files","*.xd"),("All files","*.*")])
        if not path:
            return
        try:
            with open(path, 'r') as f:
                content = f.readlines()
            # clear existing
            self.interpreter.facts.clear()
            self.interpreter.rules.clear()
            self.fact_list.delete(0, tk.END)
            self.rule_list.delete(0, tk.END)
            for line in content:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if not line.endswith('.'):
                    raise ValueError(f"Line missing trailing dot: {line}")
                text = line.rstrip('.')
                if ':-' in text:
                    hpred, hargs, body = self._parse_rule_text(text)
                    self.interpreter.rules.append((hpred, hargs, body))
                    self.rule_list.insert(tk.END, line)
                else:
                    pred, args = self._parse_fact_text(text)
                    self.interpreter.facts.setdefault(pred, set()).add(tuple(args))
                    self.fact_list.insert(tk.END, line)
        except Exception as e:
            messagebox.showerror("Load Error", str(e))

    def visualize_graph(self):
        # Build a graph of constants from facts
        G_data = nx.DiGraph()
        for pred, facts in self.interpreter.facts.items():
            for args in facts:
                if len(args) >= 2:
                    src, dst = args[0], args[1]
                    G_data.add_edge(src, dst, label=pred)
        # Build a dependency graph of predicates from rules
        G_rules = nx.DiGraph()
        for head, _, body in self.interpreter.rules:
            for p, _ in body:
                G_rules.add_edge(p, head)
        # Draw both graphs side-by-side
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))
        # Data graph
        pos1 = nx.spring_layout(G_data)
        nx.draw(G_data, pos1, ax=axs[0], with_labels=True, arrows=True, node_color='lightblue')
        edge_labels1 = nx.get_edge_attributes(G_data, 'label')
        nx.draw_networkx_edge_labels(G_data, pos1, edge_labels=edge_labels1, ax=axs[0])
        axs[0].set_title('Facts Graph')
        # Rules dependency graph
        pos2 = nx.spring_layout(G_rules)
        nx.draw(G_rules, pos2, ax=axs[1], with_labels=True, arrows=True, node_color='lightgreen')
        axs[1].set_title('Rule Dependencies')
        plt.tight_layout()
        plt.show()


def main():
    app = PrologGUI()
    app.mainloop()


if __name__ == '__main__':
    main()
