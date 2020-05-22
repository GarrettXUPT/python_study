class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(C, A):
    pass

class F(D, E):
    pass

class G(E):
    pass

class H(G, F):
    pass

'''
        求H的MRO
        设求MRO的算法的函数是L
        L(H) = H + L(G) + L(F) + GF # ECA + ECA = HGFDBECA 
        L(G) = G + L(E) + E # G + ECA + E = GECA
        L(E) = E + L(C) + L(A) + CA # E + CA + A = ECA  
        L(C) = C + L(A) + A #CA
        L(A) = A
        
        L(F) = F + L(D) + L(E) + DE # F + DBCA + ECA + DE = FDBECA
        L(D) = D + L(B) + L(C) + BC # D + BA + CA + BC  = DBCA
        L(B) = B + L(A) + A # BA
        
        # 这里的加法merge(),使用第一项的第一位和后面一项的除了第一位的每一项进行比较，如果没有出现，则该位元素算出就是前项第一位元素
          如果出现了，则此时开始下一项的第一位继续与后面的每一项除了第一位进行比较，用头部，与后续的身体去比较
        第一步：DBCA + ECA = D
        第二步： BCA + ECA = B
        第三步：  CA + ECA = E 该步骤开始，以后项E与前项的除了第一位，也就是A进行比较 
        第四步：  CA + CA = CA
        所以最终结果：DBECA

'''
print(H.__mro__)