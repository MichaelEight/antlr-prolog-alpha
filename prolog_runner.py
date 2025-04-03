from antlr4 import *
from MiniPrologLexer import MiniPrologLexer
from MiniPrologParser import MiniPrologParser
from MiniPrologVisitor import MiniPrologVisitor


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


def main():
    input_text = """
        parent(john, mary).
        parent(mary, alice).
        parent(john, lucy).
        parent(lucy, brad).
        grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

        ?- parent(X, alice).
        ?- parent(john, Y).
        ?- grandparent(john, alice).
        ?- grandparent(X, Y).
    """

    input_stream = InputStream(input_text)
    lexer = MiniPrologLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniPrologParser(token_stream)

    tree = parser.program()
    interpreter = PrologInterpreter()
    interpreter.visit(tree)


if __name__ == '__main__':
    main()
