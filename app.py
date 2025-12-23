import streamlit as st

# --- 全体のデザイン設定 ---
st.set_page_config(
    page_title="新潟1泊2日プランナー",
    page_icon="🦢",
    layout="centered"
)

# --- CSS修正：白いボタンの中の文字を「濃いオレンジ」で固定 ---
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

/* 【重要】ボタンの中の文字だけを「濃いオレンジ」に強制 */
div.stButton > button p, 
.stLinkButton a span,
.stLinkButton a div p {
    color: #FF4500 !important; /* より濃いオレンジ（朱色に近い） */
    font-weight: 900 !important; /* 極太 */
    font-size: 1.2em !important;
}

/* サイドバーの設定 */
[data-testid="stSidebar"] {
    background-color: #222222;
}
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* タブの文字 */
.stTabs [data-baseweb="tab"] {
    color: #FFFFFF !important;
}
</style>
""", unsafe_allow_html=True)

# --- アプリの中身 ---
st.title("🦢 新潟1泊2日 満喫プランナー 🦢")
st.write("2025/12/27(土)-28(日) ダウンを着て最高の聖地巡礼を！")

# --- 宿泊先情報 ---
with st.container():
    st.markdown("### 🏨 宿泊先：ホテルリブマックス新潟駅前")
    st.write("新潟駅・万代口からすぐ。拠点に最高です 。")
    st.link_button("📍 ホテルの場所をGoogleマップで見る", "https://www.google.com/maps/search/?api=1&query=ホテルリブマックス新潟駅前")

st.divider()

# タブ機能
tab1, tab2, tab3 = st.tabs(["📋 プラン作成", "🧳 持ち物リスト", "💰 予算計算"])

# --- タブ1：プラン作成 ---
with tab1:
    st.subheader("🎤 あのアーティストお気に入りのお店")
    rapper_shop = st.text_input("お店の名前を思い出したら入力してね！", placeholder="例：〇〇という居酒屋")
    
    st.subheader("今の気分は？ ✨")
    mood = st.radio("どんな旅にしたい？", ["食い倒れ！", "のんびり散策", "お洒落スポット巡り"])

    if st.button("この気分でプランを作成する！"):
        st.snow()
        
        st.subheader("🌙 1日目夜：居酒屋プラン")
        if rapper_shop:
            st.success(f"🔥 **本命：{rapper_shop}**")
            st.write("彼氏さんが言っていた「あの店」へ！年末は混み合うので予約をお忘れなく 。")
        else:
            st.info("💡 上のボックスにお店の名前を入れると、ここに表示されるよ！")

        st.write("▼ 駅前で安定して美味しい有名店はこちら")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🐟 いかの墨")
            st.link_button("📍 マップ", "https://www.google.com/maps/search/?api=1&query=いかの墨+新潟駅前店")
        with col2:
            st.markdown("### 🍶 五郎")
            st.link_button("📍 マップ", "https://www.google.com/maps/search/?api=1&query=五郎+万代店")

        # 2日目ラーメン
        st.divider()
        st.subheader("🍜 2日目ランチ：新潟ラーメン！")
        st.write("寒い日は、体を温める生姜醤油系がイチオシです 。")
        col3, col4 = st.columns(2)
        with col3:
            st.markdown("### 🍜 青島食堂 (南万代店)")
            st.link_button("📍 マップ", "https://www.google.com/maps/search/?api=1&query=青島食堂+南万代店")
        with col4:
            st.markdown("### 🍜 いっとうや (駅構内)")
            st.link_button("📍 マップ", "https://www.google.com/maps/search/?api=1&query=いっとうや+CoCoLo新潟店")

        # イルミネーション
        st.divider()
        st.subheader("✨ イルミネーション：光のページェント")
        st.write("新潟駅南口・けやき通りで開催中 。ダウンを着て歩こう ！")
        st.link_button("📍 けやき通りの場所を確認", "https://www.google.com/maps/search/?api=1&query=新潟駅南口+けやき通り")

# --- タブ2：持ち物リスト ---
with tab2:
    st.subheader("🧳 雪国への持ち物チェック")
    items = ["🧣 マフラー", "🧤 手袋", "🥾 滑りにくい靴", "🧥 ダウンジャケット", "🔋 モバイルバッテリー"]
    for item in items:
        st.checkbox(item)
    if st.button("準備完了！"):
        st.snow()

# --- タブ3：予算計算 ---
with tab3:
    st.subheader("💰 予算計算機")
    transport = st.number_input("🚄 交通費", value=20000)
    hotel_cost = st.number_input("🏨 宿泊費", value=8000)
    food_cost = st.number_input("🍖 飲食代", value=15000)
    st.metric(label="合計予想金額", value=f"{transport + hotel_cost + food_cost:,} 円")

# サイドバー
with st.sidebar:
    st.header("🌦️ お役立ち情報")
    st.link_button("☀️ Yahoo!天気（新潟市）", "https://weather.yahoo.co.jp/weather/jp/15/5410.html")
    st.write("---")
    st.write("Albirex Niigata Spirit! 🦢")
