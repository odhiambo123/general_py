# the structure :
#
# A(l.f.m.g) where
#   l is a set of instances, given instance x E l, f(x) is the set of feasible solutions
#   given an instance x and a feasiible solition y of x, m(x,y) denotes the measure of y, a positive real
#   g is the goal function which is either min or max.
#   finding some instance x an optimal solution, that is, a feasible solution y with:
#   m(x,y)=g\{m(x,y')\mid y'\in f(x)\}.
#
#   bypatrite graph.