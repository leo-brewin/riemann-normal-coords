from cadabra2_defaults import *
__cdbkernel__ = cadabra2.__cdbkernel__

__cdbtmp__ = Indices(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w#}'''), Ex(r'''position=independent)''') )

__cdbtmp__ = TableauSymmetry(Ex(r'''\Gamma^{a}_{b c}'''), Ex(r'''shape={2}, indices={1,2})''') )

__cdbtmp__ = Derivative(Ex(r'''D{#}'''), Ex(r'''''') )
__cdbtmp__ = Derivative(Ex(r'''\nabla{#}'''), Ex(r'''''') )
__cdbtmp__ = PartialDerivative(Ex(r'''\partial{#}'''), Ex(r'''''') )

__cdbtmp__ = Metric(Ex(r'''g_{a b}'''), Ex(r'''''') )
__cdbtmp__ = InverseMetric(Ex(r'''g^{a b}'''), Ex(r'''''') )

__cdbtmp__ = RiemannTensor(Ex(r'''R_{a b c d}'''), Ex(r'''''') )

__cdbtmp__ = RiemannTensor(Ex(r'''R^{a}_{b c d}'''), Ex(r'''''') )
# R_{a b c}^{d}::RiemannTensor.
__cdbtmp__ = RiemannTensor(Ex(r'''R^{a}_{b c d}'''), Ex(r'''''') )
__cdbtmp__ = RiemannTensor(Ex(r'''R^{a}_{b}^{d}_{c}'''), Ex(r'''''') )

# note: this function only covers the cases that I have seen
#       I want to keep this as short as possible
def standard_indices (obj):
    # single upstairs index on Rabcd
    substitute (obj,Ex(r'''R_{a}^{b}_{c d}   -> - R^{b}_{a c d}''', False))
    substitute (obj,Ex(r'''R_{a b}^{c}_{d}   ->   R^{c}_{d a b}''', False))
    substitute (obj,Ex(r'''R_{a b c}^{d}     -> - R^{d}_{c a b}''', False))
    # double upstairs index on Rabcd
    substitute (obj,Ex(r'''R_{a}^{b}_{c}^{d} ->   R^{b}_{a}^{d}_{c}''', False))
    substitute (obj,Ex(r'''R^{a}_{b c}^{d}   -> - R^{a}_{b}^{d}_{c}''', False))

    return obj

# note: keeping numbering as is (out of order) to ensure R appears before \nabla R etc.
def product_sort (obj):
    substitute (obj,Ex(r''' A^{a}                             -> A001^{a}                  ''', False))
    substitute (obj,Ex(r''' x^{a}                             -> A002^{a}                  ''', False))
    substitute (obj,Ex(r''' g_{a b}                           -> A003_{a b}                ''', False))
    substitute (obj,Ex(r''' g^{a b}                           -> A004^{a b}                ''', False))
    substitute (obj,Ex(r''' \nabla_{e f g h}{R_{a b c d}}     -> A011_{a b c d e f g h}    ''', False))
    substitute (obj,Ex(r''' \nabla_{e f g}{R_{a b c d}}       -> A010_{a b c d e f g}      ''', False))
    substitute (obj,Ex(r''' \nabla_{e f}{R_{a b c d}}         -> A009_{a b c d e f}        ''', False))
    substitute (obj,Ex(r''' \nabla_{e}{R_{a b c d}}           -> A008_{a b c d e}          ''', False))
    substitute (obj,Ex(r''' \partial_{e f g h}{R_{a b c d}}   -> A015_{a b c d e f g h}    ''', False))
    substitute (obj,Ex(r''' \partial_{e f g}{R_{a b c d}}     -> A014_{a b c d e f g}      ''', False))
    substitute (obj,Ex(r''' \partial_{e f}{R_{a b c d}}       -> A013_{a b c d e f}        ''', False))
    substitute (obj,Ex(r''' \partial_{e}{R_{a b c d}}         -> A012_{a b c d e}          ''', False))
    substitute (obj,Ex(r''' \partial_{e f g h}{R^{a}_{b c d}} -> A019^{a}_{b c d e f g h}  ''', False))
    substitute (obj,Ex(r''' \partial_{e f g}{R^{a}_{b c d}}   -> A018^{a}_{b c d e f g}    ''', False))
    substitute (obj,Ex(r''' \partial_{e f}{R^{a}_{b c d}}     -> A017^{a}_{b c d e f}      ''', False))
    substitute (obj,Ex(r''' \partial_{e}{R^{a}_{b c d}}       -> A016^{a}_{b c d e}        ''', False))
    substitute (obj,Ex(r''' R_{a b c d}                       -> A005_{a b c d}            ''', False))
    substitute (obj,Ex(r''' R^{a}_{b c d}                     -> A006^{a}_{b c d}          ''', False))
    substitute (obj,Ex(r''' R^{a}_{b}^{c}_{d}                 -> A007^{a}_{b}^{c}_{d}      ''', False))
    sort_product   (obj)
    rename_dummies (obj)
    substitute (obj,Ex(r''' A001^{a}                  -> A^{a}                             ''', False))
    substitute (obj,Ex(r''' A002^{a}                  -> x^{a}                             ''', False))
    substitute (obj,Ex(r''' A003_{a b}                -> g_{a b}                           ''', False))
    substitute (obj,Ex(r''' A004^{a b}                -> g^{a b}                           ''', False))
    substitute (obj,Ex(r''' A005_{a b c d}            -> R_{a b c d}                       ''', False))
    substitute (obj,Ex(r''' A006^{a}_{b c d}          -> R^{a}_{b c d}                     ''', False))
    substitute (obj,Ex(r''' A007^{a}_{b}^{c}_{d}      -> R^{a}_{b}^{c}_{d}                 ''', False))
    substitute (obj,Ex(r''' A008_{a b c d e}          -> \nabla_{e}{R_{a b c d}}           ''', False))
    substitute (obj,Ex(r''' A009_{a b c d e f}        -> \nabla_{e f}{R_{a b c d}}         ''', False))
    substitute (obj,Ex(r''' A010_{a b c d e f g}      -> \nabla_{e f g}{R_{a b c d}}       ''', False))
    substitute (obj,Ex(r''' A011_{a b c d e f g h}    -> \nabla_{e f g h}{R_{a b c d}}     ''', False))
    substitute (obj,Ex(r''' A012_{a b c d e}          -> \partial_{e}{R_{a b c d}}         ''', False))
    substitute (obj,Ex(r''' A013_{a b c d e f}        -> \partial_{e f}{R_{a b c d}}       ''', False))
    substitute (obj,Ex(r''' A014_{a b c d e f g}      -> \partial_{e f g}{R_{a b c d}}     ''', False))
    substitute (obj,Ex(r''' A015_{a b c d e f g h}    -> \partial_{e f g h}{R_{a b c d}}   ''', False))
    substitute (obj,Ex(r''' A016^{a}_{b c d e}        -> \partial_{e}{R^{a}_{b c d}}       ''', False))
    substitute (obj,Ex(r''' A017^{a}_{b c d e f}      -> \partial_{e f}{R^{a}_{b c d}}     ''', False))
    substitute (obj,Ex(r''' A018^{a}_{b c d e f g}    -> \partial_{e f g}{R^{a}_{b c d}}   ''', False))
    substitute (obj,Ex(r''' A019^{a}_{b c d e f g h}  -> \partial_{e f g h}{R^{a}_{b c d}} ''', False))

    return obj

def check (objA,objB):
    tmp  = Ex(r''' @(objA) - @(objB)'''); _=tmp 
    distribute         (tmp)
    tmp = standard_indices (tmp)
    tmp = product_sort (tmp)
    rename_dummies     (tmp)
    canonicalise       (tmp)

    return tmp
