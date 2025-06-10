#!/usr/bin/env python
# coding: utf-8

# In[1]:


def recommend_account(income, accounts):
    if "TFSA" not in accounts:
        return "建议优先开设并使用 TFSA（免税增长，无影响福利）"

    if income == "$100,000+" and "RRSP" not in accounts:
        return "你年收入较高，建议使用 RRSP 来抵税和储蓄"

    return "你已经使用了合适的账户，可进一步优化配置"

def recommend_allocation(age, risk):
    if age in ["<25", "25-34"]:
        if risk == "稳定保本":
            return "50% 股票 / 40% 债券 / 10% 现金"
        elif risk == "稍微波动但增长快":
            return "70% 股票 / 25% 债券 / 5% 现金"
        else:
            return "85% 股票 / 15% 债券"

    elif age in ["35-44", "45-54"]:
        if risk == "稳定保本":
            return "40% 股票 / 50% 债券 / 10% 现金"
        elif risk == "稍微波动但增长快":
            return "60% 股票 / 35% 债券 / 5% 现金"
        else:
            return "75% 股票 / 25% 债券"

    else:
        return "30% 股票 / 60% 债券 / 10% 现金"

def generate_tips(goal, accounts):
    tips = ""
    if goal == "买房":
        tips += "👉 可考虑开通 FHSA 账户用于首付，配合 TFSA 一起使用\n"
    if goal == "教育/子女基金":
        tips += "🎓 RESP 可获取政府配对金，强烈建议使用\n"
    if "没有/不知道" in accounts:
        tips += "📌 建议了解 TFSA / RRSP 的基本规则，错过有额度损失风险\n"
    return tips or "你目前做得不错，可以定期检查投资目标是否有变化"


# In[ ]:




