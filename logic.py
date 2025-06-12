def recommend_account(income, accounts, lang):
    has_tfsa = "TFSA" in accounts
    has_rrsp = "RRSP" in accounts
    msg = ""

    if not has_tfsa:
        msg += "建议优先开通并使用 TFSA。" if lang == "中文" else "Consider opening and using a TFSA account first.\n"

    if income == "$100,000+" and not has_rrsp:
        msg += "你年收入较高，建议使用 RRSP 来抵税。" if lang == "中文" else "With high income, using RRSP can reduce taxable income.\n"

    return msg or ("你已经使用了合适的账户。" if lang == "中文" else "Your current account setup looks good!")

def recommend_allocation(age, risk, lang):
    if age in ["<25", "25-34"]:
        if "保本" in risk or "preservation" in risk:
            return "50% 股票 / 40% 债券 / 10% 现金" if lang == "中文" else "50% stocks / 40% bonds / 10% cash"
        elif "增长快" in risk or "Moderate" in risk:
            return "70% 股票 / 25% 债券 / 5% 现金" if lang == "中文" else "70% stocks / 25% bonds / 5% cash"
        else:
            return "85% 股票 / 15% 债券" if lang == "中文" else "85% stocks / 15% bonds"

    elif age in ["35-44", "45-54"]:
        if "保本" in risk or "preservation" in risk:
            return "40% 股票 / 50% 债券 / 10% 现金" if lang == "中文" else "40% stocks / 50% bonds / 10% cash"
        elif "增长快" in risk or "Moderate" in risk:
            return "60% 股票 / 35% 债券 / 5% 现金" if lang == "中文" else "60% stocks / 35% bonds / 5% cash"
        else:
            return "75% 股票 / 25% 债券" if lang == "中文" else "75% stocks / 25% bonds"

    else:
        return "30% 股票 / 60% 债券 / 10% 现金" if lang == "中文" else "30% stocks / 60% bonds / 10% cash"

def generate_tips(goal, accounts, lang):
    tips = ""
    if goal in ["买房", "Buying a home"]:
        tips += "👉 可以开通 FHSA，享受首付免税储蓄。\n" if lang == "中文" else "👉 Consider FHSA for tax-free home savings.\n"
    if goal in ["教育/子女基金", "Education fund"]:
        tips += "🎓 RESP 可获得政府补贴。\n" if lang == "中文" else "🎓 RESP provides government grants.\n"
    if "没有/不知道" in accounts or "None" in accounts:
        tips += "📌 建议尽快了解 TFSA / RRSP 的基本规则。\n" if lang == "中文" else "📌 It's important to learn the basics of TFSA/RRSP soon.\n"
    return tips or ("你目前做得不错，可保持现有策略。" if lang == "中文" else "You're on a good track. Stay consistent!")
