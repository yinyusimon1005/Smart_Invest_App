import streamlit as st
from logic import recommend_account, recommend_allocation, generate_tips

# 页面设置
st.set_page_config(page_title="Smart Invest 智能理财助手", layout="centered")
st.title("🏡 Smart Invest  智能理财推荐")

# --- 多语言切换 ---
lang = st.radio("选择语言 / Choose Language", ["中文", "English"])

# --- 邮箱收集 ---
email = st.text_input("留下你的邮箱，获取PDF报告 / Enter email to receive your report (optional):")

# 简单邮箱格式检查
if email and "@" not in email:
    st.warning("邮箱格式错误，请重新输入。" if lang == "中文" else "Invalid email format, please re-enter.")

# --- 表单输入 ---
with st.form("user_profile"):
    age = st.selectbox("你的年龄是多少？" if lang == "中文" else "Your age:",
                       ["<25", "25-34", "35-44", "45-54", "55+"])
    income = st.selectbox("年收入（税前）：" if lang == "中文" else "Annual income (before tax):",
                          ["<$40,000", "$40,000-$70,000", "$70,000-$100,000", "$100,000+"])
    risk = st.radio("你更看重什么？" if lang == "中文" else "What do you value more?",
                    ["稳定保本", "稍微波动但增长快", "我能承受亏损，追求高增长"]
                    if lang == "中文"
                    else ["Capital preservation", "Moderate growth", "High risk & growth"])
    accounts = st.multiselect("你目前拥有的账户：" if lang == "中文" else "Accounts you currently have:",
                              ["TFSA", "RRSP", "RESP", "非注册账户", "没有/不知道"]
                              if lang == "中文"
                              else ["TFSA", "RRSP", "RESP", "Non-registered", "None/Not sure"])
    goal = st.selectbox("你的财务目标是？" if lang == "中文" else "Your financial goal:",
                        ["买房", "教育/子女基金", "提前退休", "一般储蓄/增长"]
                        if lang == "中文"
                        else ["Buying a home", "Education fund", "Early retirement", "General savings/growth"])

    submitted = st.form_submit_button("🔍 获取建议" if lang == "中文" else "🔍 Get Recommendation")

# --- 结果输出 ---
if submitted:
    st.subheader("📊 推荐报告" if lang == "中文" else "📊 Personalized Report")

    acc_text = recommend_account(income, accounts, lang)
    alloc_text = recommend_allocation(age, risk, lang)
    tips_text = generate_tips(goal, accounts, lang)

    st.markdown("### 💼 推荐账户" if lang == "中文" else "### 💼 Recommended Accounts")
    st.info(acc_text)

    st.markdown("### 📈 投资配置建议" if lang == "中文" else "### 📈 Asset Allocation")
    st.success(alloc_text)

    st.markdown("### 💡 理财建议" if lang == "中文" else "### 💡 Smart Tips")
    st.write(tips_text)

    # ✅ 打印提示代替 PDF 下载
    # PDF 打印提示（根据语言）
    print_tip = (
        "📄 如需保存整个推荐报告为 PDF，请点击网页右上角菜单（⋮），选择 **Print / 打印**，然后选择 **保存为 PDF**。请确保在“更多设置”中勾选 ✅ **打印背景图形**，以保留颜色和样式。"
        if lang == "中文"
        else "📄 To save the full report as a PDF, click the top-right menu (⋮), select **Print**, then choose **Save as PDF**. Make sure to check ✅ **Print background graphics** under 'More settings' to preserve color and layout."
    )
    st.info(print_tip, icon="💡")
