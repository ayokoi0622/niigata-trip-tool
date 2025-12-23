import streamlit as st
from datetime import date

# --- デザイン設定（白鳥アイコン 🦢） ---
st.set_page_config(
    page_title="新潟1泊2日プランナー",
    page_icon="🦢",
    layout="centered"
)

# --- CSS：オレンジ背景 ＋ 白ボタン ＋ 濃いオレンジ太文字 ---
st.markdown("""
<style>
/* 背景：アルビオレンジ */
.stApp {
    background-color: #FF8C00; 
}

/* 基本のテキストを白に */
h1, h2, h3, p, span, label, li, .stMarkdown {
    color: #FFFFFF !important;
}

/* 【重要】白いボタン自体の設定 */
div.stButton > button, .stLinkButton a {
    background-color: #FFFFFF !important;
    border-radius: 20px !important;
    border: none !important;
    width: 100% !important;
    height: 3.5em !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-decoration: none !important;
}

/* 【重要】ボタンの中の文字を「濃いオレンジ」で固定 */
div.stButton > button p, 
.stLinkButton a span,
.stLinkButton a div p {
    color: #FF4500 !important;
    font-weight: 900 !important;
    font-size: 1.1em !important;
}

/* サイドバーの設定 */
[data-testid="stSidebar"] {
    background-color: #222222;
}
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* タブのデザイン */
.stTabs [data-baseweb="tab"] {
    color: #FFFFFF !important;
}
</style>
""", unsafe_allow_html=True)

# --- カウントダウン機能 ---
trip_date = date(2025, 12, 27)
today = date.today()
days_left = (trip_date - today).days

st.title("🦢 新潟1泊2日 プランナー 🦢")
if days_left > 0:
    st.subheader(f"🚀 始まりまであと **{days_left}** 日")
elif days_left == 0:
    st.subheader("🎉 ついに当日！")
else:
    st.subheader("❄️ 新潟の旅はいかがですか？")

st.divider()

# タブ機能
tab1, tab2, tab3, tab4 = st.tabs(["📋 プラン", "🧳 持ち物", "💰 予算", "🍶 日本酒メモ"])

# --- タブ1：プラン & タイムライン（20:00帰路に修正） ---
with tab1:
    st.subheader("⏰ スケジュール")
    with st.expander("📅 1日目の流れ（12/27）"):
        st.write("・11:00 新潟駅着（ホテルに荷物預ける） → ピア万代でランチ🐟")
        st.write("・13:00 万代シテイをぶらぶら")
        st.write("・15:00 ホテルにチェックイン🏨")
        st.write("・18:00 居酒屋へ🏮")
        st.write("・20:30 けやき通りのイルミネーション散歩")

    with st.expander("📅 2日目の流れ（12/28）"):
        st.write("・10:00 ゆっくりチェックアウト")
        st.write("・12:00 新潟ラーメンランチ🍜")
        st.write("・14:30 駅ビルでお土産探し🐟")
        st.write("・17:30 最後に駅前でもう一杯(ぽんしゅ館)🍶")
        st.write("・20:00 新幹線で東京へ（お疲れ様でした！）🚄")

    st.subheader("あの店を思い出した？")
    # 呼称を「彼」に修正
    rapper_shop = st.text_input("お店（メモ）", placeholder="居酒屋の名前がわかったらここに入力！")
    
    if st.button("プランの詳細を表示する！"):
        st.snow()
        if rapper_shop:
            st.success(f"🔥 **本命：{rapper_shop}**")
            st.write("「あの店」へ！")
        else:
            st.info("💡 上のボックスにお店の名前を入れると、ここに表示されるよ")

        st.subheader("🍜 2日目ランチ：新潟ラーメン")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("🍜 青島食堂 (生姜醤油)", "https://www.google.com/maps/search/?api=1&query=青島食堂+南万代店")
        with col2:
            st.link_button("🍜 いっとうや (人気店)", "https://www.google.com/maps/search/?api=1&query=いっとうや+CoCoLo新潟店")

        st.subheader("✨ イルミネーション")
        st.link_button("📍 けやき通りの場所を確認", "https://www.google.com/maps/search/?api=1&query=新潟駅南口+けやき通り+イルミネーション")

# --- タブ2：持ち物リスト ---
with tab2:
    st.subheader("🧳 雪国への準備")
    items = ["🧣 マフラー", "🧤 手袋", "🥾 滑りにくい靴", "🧥 ダウンジャケット", "🔋 モバイルバッテリー"]
    for item in items:
        st.checkbox(item)
    if st.button("準備完了！"):
        st.snow()

# --- タブ3：予算計算 ---
with tab3:
    st.subheader("💰 予算シミュレーション")
    transport = st.number_input("🚄 交通費", value=20000)
    hotel_cost = st.number_input("🏨 宿泊費", value=6000)
    food_cost = st.number_input("🍖 飲食代", value=15000)
    st.metric(label="合計予想金額", value=f"{transport + hotel_cost + food_cost:,} 円")

# --- タブ4：日本酒メモ ---
with tab4:
    st.subheader("🍶 ぽんしゅ館・利き酒メモ")
    sake_name = st.text_input("飲んだお酒の名前")
    sake_score = st.slider("評価", 1, 5, 3)
    if st.button("メモを保存"):
        st.write(f"📝 **{sake_name}** ({'⭐' * sake_score})")

# サイドバー
with st.sidebar:
    st.header("🌦️ 寒さ・移動対策")
    st.link_button("☀️ Yahoo!天気（新潟市）", "https://weather.yahoo.co.jp/weather/jp/15/5410.html")
    st.write("---")
    st.link_button("🚕 GO（タクシー配車）", "https://go.goinc.jp/")
    st.write("---")
  
