import streamlit as st

# --- 全体のデザイン設定（白鳥アイコン 🦢） ---
st.set_page_config(
    page_title="新潟1泊2日プランナー",
    page_icon="🦢",
    layout="centered"
)

# --- オレンジ×ホワイト（視認性重視）CSS ---
st.markdown("""
<style>
/* 背景：アルビオレンジ */
.stApp {
    background-color: #FF8C00; 
}

/* テキスト全般を白に */
h1, h2, h3, p, span, label, li, .stMarkdown {
    color: #FFFFFF !important;
}

/* ボタン：白地にオレンジ文字でハッキリさせる */
div.stButton > button, .stLinkButton a {
    background-color: #FFFFFF !important;
    color: #FF8C00 !important;
    border-radius: 20px !important;
    border: none !important;
    font-weight: bold !important;
    display: inline-flex !important;
    justify-content: center !important;
    align-items: center !important;
    padding: 10px 20px !important;
    text-decoration: none !important;
    min-height: 45px !important;
}

/* サイドバーの中の文字も白く */
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* タブの見た目 */
.stTabs [data-baseweb="tab"] {
    color: #FFFFFF !important;
}
.stTabs [aria-selected="true"] {
    border-bottom-color: #FFFFFF !important;
    font-weight: bold !important;
}

/* 入力欄のラベル色 */
.stSelectbox label, .stRadio label, .stNumberInput label, .stCheckbox label {
    color: #FFFFFF !important;
}
</style>
""", unsafe_allow_html=True)

# --- アプリの中身 ---
st.title("🦢 新潟1泊2日 満喫プランナー 🦢")
st.write("2025/12/27(土)-28(日) の新潟旅行へ！")

# --- 宿泊先情報（地図ボタン修正） ---
with st.container():
    st.markdown("### 🏨 宿泊先：ホテルリブマックス新潟駅前")
    st.write("新潟駅・万代口から徒歩圏内。拠点に最高です 。")
    # 地図ボタン
    st.link_button("📍 ホテルの地図をGoogleマップで開く", 
                   "https://www.google.com/maps/search/?api=1&query=ホテルリブマックス新潟駅前")

st.divider()

# タブ機能
tab1, tab2, tab3 = st.tabs(["📋 プラン作成", "🧳 持ち物リスト", "💰 予算計算"])

with tab1:
    st.subheader("今の気分は？ ✨")
    mood = st.radio("Q1. どんな旅にしたい？", ["食い倒れ！", "のんびり散策", "お洒落スポット巡り"])
    lunch_pref = st.selectbox("Q2. 2日目のランチは？", ["贅沢海鮮", "タレかつ/へぎそば", "お洒落カフェ"])

    if st.button("この気分でプランを作成する！"):
        st.balloons()
        
        st.subheader("🌙 1日目夜：おすすめ居酒屋")
        st.write("年末は混み合うので今すぐ予約を ！")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🐟 いかの墨")
            st.link_button("📍 マップを開く", "https://www.google.com/maps/search/?api=1&query=いかの墨+新潟駅前店")
        with col2:
            st.markdown("### 🍶 五郎")
            st.link_button("📍 マップを開く", "https://www.google.com/maps/search/?api=1&query=五郎+万代店")

        st.subheader("✨ イルミネーション：光のページェント")
        st.write("駅南口・けやき通りで開催中！防寒を忘れずに 。")
        st.link_button("📍 けやき通りの地図", "https://www.google.com/maps/search/?api=1&query=新潟駅南口+けやき通り+イルミネーション")

with tab2:
    st.subheader("🧳 雪国への持ち物チェック")
    items = ["🧣 マフラー", "🧤 手袋", "🥾 滑らない靴", "🧥 厚手のコート", "🔋 モバッテリー"]
    for item in items:
        st.checkbox(item)

with tab3:
    st.subheader("💰 予算計算機")
    transport = st.number_input("🚄 交通費", value=20000)
    hotel = st.number_input("🏨 宿泊費", value=8000)
    food = st.number_input("🍖 飲食・お土産", value=15000)
    st.metric(label="合計予想金額", value=f"{transport + hotel + food:,} 円")

# サイドバー：天気予報リンク
with st.sidebar:
    st.header("🌦️ お役立ち情報")
    # 文字が見えるようにリンクをボタン化
    st.link_button("🌡️ 新潟市の天気予報を見る", "https://tenki.jp/forecast/4/18/47604/15100/")
    st.write("---")
    st.write("Albirex Niigata Spirit! 🦢")
