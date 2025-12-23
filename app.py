import streamlit as st

# --- 全体のデザイン設定（白鳥アイコン 🦢） ---
st.set_page_config(
    page_title="新潟1泊2日プランナー",
    page_icon="🦢",
    layout="centered"
)

# --- CSS：オレンジ背景 ＋ 白ボタン ＋ オレンジ太文字 ---
st.markdown("""
<style>
.stApp { background-color: #FF8C00; }
h1, h2, h3, p, span, label, li, .stMarkdown { color: #FFFFFF !important; }
div.stButton > button, .stLinkButton a {
    background-color: #FFFFFF !important;
    border-radius: 20px !important;
    border: none !important;
    width: 100% !important;
    height: 3.5em !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
div.stButton > button p, .stLinkButton a span {
    color: #FF8C00 !important;
    font-weight: bold !important;
    font-size: 1.1em !important;
}
[data-testid="stSidebar"] { background-color: #333333; }
[data-testid="stSidebar"] * { color: #FFFFFF !important; }
.stTabs [data-baseweb="tab"] { color: #FFFFFF !important; }
</style>
""", unsafe_allow_html=True)

# --- アプリの中身 ---
st.title("🦢 新潟1泊2日 満喫プランナー 🦢")
st.write("2025/12/27(土)-28(日) 大切な思い出の地を巡る旅")

# --- 宿泊先情報 ---
with st.container():
    st.markdown("### 🏨 宿泊先：ホテルリブマックス新潟駅前")
    st.link_button("📍 ホテルの場所をGoogleマップで見る", "https://www.google.com/maps/search/?api=1&query=ホテルリブマックス新潟駅前")

st.divider()

# タブ機能
tab1, tab2, tab3 = st.tabs(["📋 プラン作成", "🧳 持ち物リスト", "💰 予算計算"])

# --- タブ1：プラン作成 ---
with tab1:
    st.subheader("🎤 あのアーティストお気に入りのお店")
    # メモ機能：ここに入力した文字が下のプランに反映されます
    rapper_shop = st.text_input("お店の名前を思い出したら入力してね！", placeholder="例：〇〇という居酒屋")
    
    st.subheader("今の気分は？ ✨")
    mood = st.radio("どんな旅にしたい？", ["食い倒れ！", "のんびり散策", "お洒落スポット巡り"])

    if st.button("この気分でプランを作成する！"):
        st.snow() # 雪を降らせます！
        
        # 1日目夜の案内
        st.subheader("🌙 1日目夜：居酒屋プラン")
        
        if rapper_shop:
            st.success(f"🔥 **本命：{rapper_shop}**")
            st.write("彼氏さんが言っていた「あの店」へ！最高の夜になりますように！")
        else:
            st.info("💡 上のボックスにお店の名前を入力すると、ここに表示されるよ！")

        st.write("▼ もし予約が取れなかった時のためのバックアップ店")
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
        st.write("寒い日はやっぱりラーメン！人気店をピックアップしました。")
        col3, col4 = st.columns(2)
        with col3:
            st.markdown("### 🍜 青島食堂 (生姜醤油)")
            st.link_button("📍 マップ", "https://www.google.com/maps/search/?api=1&query=五郎+万代店+新潟県新潟市中央区東大通2-3-153")
        with col4:
            st.markdown("### 🍜 いっとうや (人気店)")
            st.link_button("📍 マップ", "https://www.google.com/maps/search/?api=1&query=五郎+万代店+新潟県新潟市中央区東大通2-3-154")

        # イルミネーション
        st.divider()
        st.subheader("✨ イルミネーション：光のページェント")
        st.write("駅南口・けやき通りで開催中。ダウンを着て歩こう！")
        st.link_button("📍 場所を確認", "https://www.google.com/maps/search/?api=1&query=新潟駅南口+けやき通り+イルミネーション")

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
    hotel = st.number_input("🏨 宿泊費", value=8000)
    food = st.number_input("🍖 飲食代", value=15000)
    st.metric(label="合計予想金額", value=f"{transport + hotel + food:,} 円")

# サイドバー
with st.sidebar:
    st.header("🌦️ お役立ち情報")
    st.link_button("☀️ Yahoo!天気（新潟市）", "https://weather.yahoo.co.jp/weather/jp/15/5410.html")
    st.write("---")
    st.write("Albirex Niigata Spirit! 🦢")
