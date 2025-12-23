import streamlit as st

# --- 全体のデザイン設定 ---
st.set_page_config(
    page_title="新潟1泊2日プラン",
    page_icon="🦢",
    layout="centered"
)

# --- CSS修正：ボタンの中の文字をオレンジに固定 ---
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

/* 【重要】ボタンの設定：白地にオレンジの太文字 */
div.stButton > button, .stLinkButton a {
    background-color: #FFFFFF !important;
    border-radius: 20px !important;
    border: none !important;
    width: 100% !important;
    height: 3em !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-decoration: none !important;
}

/* ボタンの中のテキストだけをオレンジ色に強制 */
div.stButton > button div p, 
div.stButton > button p,
.stLinkButton a span,
.stLinkButton a div p {
    color: #FF8C00 !important;
    font-weight: bold !important;
    font-size: 1.1em !important;
}

/* サイドバーの背景と文字 */
[data-testid="stSidebar"] {
    background-color: #333333; /* サイドバーはあえて濃い色で引き締め */
}
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* タブのデザイン */
.stTabs [data-baseweb="tab"] {
    color: #FFFFFF !important;
}
.stTabs [aria-selected="true"] {
    background-color: rgba(255,255,255,0.2) !important;
    border-radius: 10px 10px 0 0 !important;
}
</style>
""", unsafe_allow_html=True)

# --- アプリの中身 ---
st.title("🦢 新潟1泊2日 満喫プランナー 🦢")
st.write("2025/12/27(土)-28(日) の新潟旅行へ！")

# --- 宿泊先情報 ---
with st.container():
    st.markdown("### 🏨 宿泊先：ホテルリブマックス新潟駅前")
    st.write("新潟駅・万代口から徒歩圏内。拠点に最高 。")
    # ホテル地図ボタン
    st.link_button("📍 ホテルの場所をGoogleマップで見る", "https://www.google.com/maps/search/?api=1&query=ホテルリブマックス新潟駅前")

st.divider()

# タブ機能
tab1, tab2, tab3 = st.tabs(["📋 プラン作成", "🧳 持ち物リスト", "💰 予算計算"])

with tab1:
    st.subheader("今の気分は？ ✨")
    mood = st.radio("Q1. どんな旅にしたい？", ["食い倒れ！", "のんびり散策", "お洒落スポット巡り"])
    lunch_pref = st.selectbox("Q2. 2日目のランチは？", ["贅沢海鮮", "タレかつ/へぎそば", "お洒落カフェ"])

    if st.button("この気分でプランを作成する！"):
        st.snow()
        
        st.subheader("🌙 1日目夜：おすすめ居酒屋")
        st.write("年末は非常に混み合うので今すぐ予約を ！")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🐟 いかの墨")
            st.link_button("📍 マップを開く", "https://www.google.com/maps/search/?api=1&query=いかの墨+新潟駅前店")
        with col2:
            st.markdown("### 🍶 五郎")
            st.link_button("📍 マップを開く", "https://www.google.com/maps/search/?api=1&query=五郎+万代店")

        st.subheader("✨ イルミネーション")
        st.write("駅南口・けやき通りで開催中！防寒対策を万全に 。")
        st.link_button("📍 けやき通りの場所を確認", "https://www.google.com/maps/search/?api=1&query=新潟駅南口+けやき通り")

with tab2:
    st.subheader("🧳 雪国への持ち物チェック")
    items = ["🧣 マフラー", "🧤 手袋", "🥾 滑りにくい靴", "🧥 厚手のコート", "🔋 モバイルバッテリー"]
    for item in items:
        st.checkbox(item)

with tab3:
    st.subheader("💰 予算計算機")
    transport = st.number_input("🚄 交通費", value=20000)
    hotel = st.number_input("🏨 宿泊費", value=8000)
    food = st.number_input("🍖 食費・お土産", value=15000)
    st.metric(label="合計予想金額", value=f"{transport + hotel + food:,} 円")

# サイドバー：Yahoo!天気
with st.sidebar:
    st.header("🌦️ お役立ち情報")
    # Yahoo!天気 新潟市のページ
    st.link_button("☀️ Yahoo!天気（新潟市）", "https://weather.yahoo.co.jp/weather/jp/15/5410.html")
    st.write("---")
    
