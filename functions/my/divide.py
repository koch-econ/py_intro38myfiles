
#%%
def divide(numerator, denominator) :
    return numerator / denominator
#%%
2+2
divide(10, 2)
#%%
divide(numerator =10, denominator=2)
#%%
divide(denominator=2, numerator=10)
#%%
divide(10, denominator=2)
#%%
def div2(numerator,*, denominator) :
    return numerator / denominator
#%%
divide(10, denominator=2)
# %%
'*'
#%%
div2(10, 2)

#%%
def div3(numerator,/, denominator) :
    return numerator / denominator
#%%
div3(10, 2)
#%%
div3(numerator =10, denominator=2)
# %%
div3(10, denominator=2)

# %%
