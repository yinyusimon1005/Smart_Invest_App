#!/usr/bin/env python
# coding: utf-8

# In[5]:

# import packages

import streamlit as st
from logic import recommend_account, recommend_allocation, generate_tips

st.set_page_config(page_title="SmartInvest", layout="centered")
st.title("🏡 SmartInvest 加拿大理财推荐")

st.markdown("为你量身打造的 TFSA / RRSP / 配置建议 —— 简单 3 分钟")

# --- 表单输入 ---
with st.form("user_profile"):
    age = st.selectbox("你的年龄", ["<25", "25-34", "35-44", "45-54", "55+"])
    income = st.selectbox("你的年收入（税前）", ["<$40,000", "$40,000-$70,000", "$70,000-$100,000", "$100,000+"])
    risk = st.radio("你更看重什么？", ["稳定保本", "稍微波动但增长快", "我能承受亏损，追求高增长"])
    accounts = st.multiselect("你目前拥有的账户", ["TFSA", "RRSP", "RESP", "非注册账户", "没有/不知道"])
    goal = st.selectbox("你的未来主要目标是", ["买房", "教育/子女基金", "提前退休", "一般储蓄/增长"])
    submitted = st.form_submit_button("🔍 获取建议")

# --- 输出部分 ---
if submitted:
    st.subheader("📊 你的个性化理财建议")

    st.markdown("### 💼 推荐账户使用顺序")
    st.info(recommend_account(income, accounts))

    st.markdown("### 📈 资产配置建议")
    st.success(recommend_allocation(age, risk))

    st.markdown("### 💡 理财小贴士")
    st.write(generate_tips(goal, accounts))


# In[ ]:




