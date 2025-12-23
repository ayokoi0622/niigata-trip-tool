import streamlit as st

# --- 全体のデザイン設定 ---
st.set_page_config(
    page_title="新潟1泊2日プランナー",
    page_icon="🍊",
    layout="centered"
)

# --- 背景オレンジ・文字ホワイトのカスタムCSS ---
st.markdown("""
<style>
/* アプリ全体の背景を鮮やかなオレンジに */
.stApp {
    background-color: #FF8C00; /* ダークオレンジ */
}

/* すべてのテキスト（見出し、本文、ラベル）を白に固定 */
h1, h2, h3, p, span, label, li, .stMarkdown, .stSelectbox label, .stRadio label, .stNumberInput label, .stCheckbox label {
    color: #FFFFFF !important;
    font-weight: 500;
}

/* タブの文字も白に */
.stTabs [data-baseweb="tab"] {
    color: #FFFFFF !important;
}

/* ボタンは白背景にオレンジ文字 */
div.stButton > button {
    background-color: #FFFFFF;
    color: #FF8C00;
    border-radius: 20px;
    border: none;
    font-weight: bold;
    width: 100%;
}
div.stButton > button:hover {
    background-color: #FFE4B5;
    color: #FF8C00;
}

/* リンクボタンのデザイン */
.stElementContainer a {
    background-color: #FFFFFF !important;
    color: #FF8C00 !important;
    font-weight: bold !important;
    border-radius: 20px !important;
}

/* 成功メッセージなどの枠線を調整 */
.stAlert {
    background-color: rgba(255, 255, 255, 0.2) !important;
    color: white !important;
    border: 1px solid white !important;
}
</style>
""", unsafe_allow_html=True)


# --- メインコンテンツ ---
st.title("🍊 新潟1泊2日 満喫プランナー 🍊")
st.write("2025/12/27(土)-28(日) の旅行を楽しみましょう！")

# --- 宿泊先情報（地図ボタン追加） ---
with st.container():
    st.success("🏨 **宿泊先：ホテルリブマックス新潟駅前**")
    st.write("新潟駅・万代口から徒歩圏内でアクセス抜群です。")
    # ホテルリブマックス新潟駅前の地図URL
    st.link_button("📍 ホテルの場所をGoogleマップで見る", "https://maps.google.com/?cid=2896416919245910711&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ")

st.divider()

# タブ機能
tab1, tab2, tab3 = st.tabs(["📋 プラン作成", "🧳 持ち物リスト", "💰 予算計算"])

# --- タブ1：プラン作成 ---
with tab1:
    st.subheader("今の気分は？ ✨")
    mood = st.radio("Q1. どんな旅にしたい？", ["食い倒れ！", "のんびり散策", "お洒落スポット巡り"])
    lunch_pref = st.selectbox("Q2. 2日目のランチは？", ["贅沢海鮮", "タレかつ/へぎそば", "お洒落カフェ"])

    if st.button("この気分でプランを作成する！"):
        st.balloons()
        
        # 1日目夜の居酒屋案内
        st.subheader("🌙 1日目夜：新潟駅前の名店（要予約！）")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🐟 いかの墨 新潟駅前店")
            st.write("最高ののどぐろと地酒を堪能！")
            st.link_button("📍 マップで見る", "https://maps.google.com/?cid=7115428728919781949&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ")
        with col2:
            st.markdown("### 🍶 五郎 万代店")
            st.write("地元民も通う活気ある居酒屋。")
            st.link_button("📍 マップで見る", "https://maps.google.com/?cid=12156854267396659778&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ")

        # イルミネーション案内
        st.divider()
        st.subheader("✨ イルミネーション：光のページェント")
        st.write("新潟駅南口のけやき通りが16万球の光に包まれます。")
        st.link_button("📍 けやき通りの場所を確認", "https://maps.google.com/?cid=7159820495602100329&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQ")

        # コース詳細
        st.divider()
        if mood == "食い倒れ！":
            st.write("**【1日目】** ぽんしゅ館で利き酒 → ピアBandaiで海鮮 → 夜は予約した居酒屋へ！")
            st.write(f"**【2日目】** 古町エリアを散策 → ランチ：{lunch_pref} → 駅ビルでお土産")
        else:
            st.write("**【1日目】** 万代シテイで買い物 → 信濃川沿いを散歩 → 夜は居酒屋へ！")
            st.write(f"**【2日目】** 朱鷺メッセ展望室で絶景 → ランチ：{lunch_pref} → 最後にぽんしゅ館")

# --- タブ2：持ち物リスト ---
with tab2:
    st.subheader("🧳 雪国への準備（チェックしてね）")
    items = ["🧣 マフラー・ストール", "🧤 手袋", "🥾 滑りにくい靴", "🧥 厚手のコート", "🔋 モバイルバッテリー", "💊 カイロ"]
    for item in items:
        st.checkbox(item)
    
    if st.button("準備バッチリ！"):
        st.balloons()

# --- タブ3：予算計算 ---
with tab3:
    st.subheader("💰 予算シミュレーション")
    transport = st.number_input("🚄 交通費", value=20000, step=1000)
    hotel_cost = st.number_input("🏨 宿泊費", value=8000, step=1000)
    food_cost = st.number_input("🍖 食費・雑費", value=15000, step=1000)
    
    total = transport + hotel_cost + food_cost
    st.divider()
    st.metric(label="合計予想金額", value=f"{total:,} 円")
    st.write("※予算に合わせて計画を立てましょう！")

# サイドバー
with st.sidebar:
    st.header("🌡️ お役立ち情報")
    st.link_button("新潟市の天気予報 (tenki.jp)", "https://tenki.jp/forecast/4/18/47604/15100/")
    st.write("---")
    st.write("Have a nice trip to Niigata! ❄️")
