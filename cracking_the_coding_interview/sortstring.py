# -*- coding:utf-8 -*-
'''
请编写一个方法，对一个字符串数组进行排序，将所有变位词合并，保留其字典序最小的一个串。
这里的变位词指变换其字母顺序所构成的新的词或短语。
例如"triangle"和"integral"就是变位词
'''
class SortString:
  def sortStrings(self, s, n):
    s_dict = {}
    for string in s:
      key = "".join((lambda x:(x.sort(),x)[1])(list(string)))
      if key not in s_dict.keys() or string < s_dict[key]:
        s_dict[key] = string

    s = list(s_dict.values())
    s.sort()
    return s

# testcase
s = ["emmaldzsvjggzfoda","skmjhsm","zjwmkgufsvwrwyvrhk","vyksgrwwjmwrhzfvuk","wfszrykvjrmuwhkvgw","kwrwuwjvksyvhmrzfg","kom","mko","mko","nezrxmdjgjqexmqz","gjmqdrzqzjeemxxn","qqxedgjjmrznmxez","xxgmjezerjnqmzdq","vwcmmngdsvzx","xvmdvwscgnmz","msnvvczxdgwm","izmvzrhltsiubcukc","cslnzuenr","rznulsenc","lnsnucrez","gkyfvvni","gikvvynf","ivkfyvng","vygfvikn","nwxkeyhnvniquhpapw","wnhyknvanhepwquxip","rrpujexoukmmrnmpdzcf","ksirghrnjx","ixrhgkrnjs","kup","kpu","kpu","emnetqjwnfwi","qpozvklf","qpvkolfz","flpkvoqz","zlkpvfoq","zldjqciktnevrkb","vklqjdrktcebizn","ntrqkvebiljczkd","nkktcebjirqvldz","mytegbucud","gbtcyuemud","gctmuedybu","ahgeomesgcehvk","oamshhecevggek","gmcekevoehsahg","gvgeacmheeoksh","ma","am","am","wxdyddyrenzsylfwx","syedwdylxrwfyxzdn","dwsddyelxywrxyfnz","rdrrfuowxukryfmli","qdjzmdobajs","ymysuotfxpboc","awzccscrkozbhygrkvv","ovrgybhswrczzkcacvk","zcrwkyhrzkgacvsocbv","vzwgzosrkvkcrcybahc","ftytv","ttvyf","tfyvt","vtytf","pggunxuyduy","qijygauutkt","aytqutkugji","itjutqugaky","nfoenumvnmannkkhmueo","ounmkhknefvemnmannou","eonmenfkhmuaonnnumvk","mvnouemekonfamnnnhku","a"]
n = 74
res = ["a","ahgeomesgcehvk","am","awzccscrkozbhygrkvv","aytqutkugji","cslnzuenr","dwsddyelxywrxyfnz","emmaldzsvjggzfoda","emnetqjwnfwi","eonmenfkhmuaonnnumvk","flpkvoqz","ftytv","gbtcyuemud","gikvvynf","gjmqdrzqzjeemxxn","ixrhgkrnjs","izmvzrhltsiubcukc","kom","kpu","kwrwuwjvksyvhmrzfg","msnvvczxdgwm","nkktcebjirqvldz","nwxkeyhnvniquhpapw","pggunxuyduy","qdjzmdobajs","rdrrfuowxukryfmli","rrpujexoukmmrnmpdzcf","skmjhsm","ymysuotfxpboc"]
print(SortString().sortStrings(s, n) == res)