import streamlit as st
from datetime import date

# --- デザイン設定 ---
st.set_page_config(page_title="新潟1泊2日プランナー", page_icon="Swan", layout="centered")

# --- CSS：オレンジ背景 ＋ 白ボタン ＋ オレンジ太文字（修正版） ---
st.markdown("""
<style>
.stApp { background-color: #FF8C00; }
h1, h2, h3, p, span, label, li, .stMarkdown { color: #FFFFFF !important; }
div.stButton > button, .stLinkButton a {
    background-color: #FFFFFF !important;
    border-radius: 20px !important;
    border: none !important;
    width: 100% !important;
}
div.stButton > button p, .stLinkButton a span {
    color: #FF4500 !important;
    font-weight: 900 !important;
}
[data-testid="stSidebar"] { background-color: #222222; }
[data-testid="stSidebar"] * { color: #FFFFFF !important; }
</style>
""", unsafe_allow_html=True)

# --- 1. カウントダウン機能 ---
trip_date = date(2025, 12, 27)
today = date.today()
days_left = (trip_date - today).days

st.title("🦢 新潟1泊2日 満喫プランナー 🦢")
if days_left > 0:
    st.subheader(f"🚀 旅行まであと **{days_left}** 日！")
elif days_left == 0:
    st.subheader("🎉 ついに旅行当日です！楽しんで！")
else:
    st.subheader("❄️ 新潟旅行を楽しんでいますか？")

st.divider()

# タブ機能
tab1, tab2, tab3, tab4 = st.tabs(["📋 プラン", "🧳 持ち物", "💰 予算", "🍶 日本酒メモ"])

# --- タブ1：プラン & タイムライン ---
with tab1:
    st.subheader("⏰ スケジュール")
    with st.expander("📅 1日目の流れ（12/27）"):
        st.write("・11:00 新潟駅着 → ぽんしゅ館🍶")
        st.write("・13:00 万代エリアでショッピング🛍️")
        st.write("・15:00 ホテルリブマックスに荷物を置く🏨")
        st.write("・18:00 彼氏さん本命のお店 or 居酒屋🏮")
        st.write("・20:00 けやき通りのイルミネーション✨")

    with st.expander("📅 2日目の流れ（12/28）"):
        st.write("・10:00 チェックアウト")
        st.write("・11:30 念願の新潟ラーメンランチ🍜")
        st.write("・14:00 ピアBandaiでお土産探し🐟")
        st.write("・16:00 新幹線で帰路へ🚄")

    st.subheader("🎤 あの店を思い出した？")
    rapper_shop = st.text_input("お店の名前を入力！", placeholder="例：〇〇という居酒屋")
    
    if st.button("プランの詳細を表示する！"):
        st.snow()
        if rapper_shop:
            st.success(f"🔥 **本命：{rapper_shop}**")
        st.markdown("### 🍜 2日目ランチ候補：新潟5大ラーメン")
        st.write("生姜醤油ラーメンは体が温まって冬に最適です。")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("🍜 青島食堂", "https://www.google.com/maps/search/?api=1&query=青島食堂+南万代店")
        with col2:
            st.link_button("🍜 いっとうや", "https://www.google.com/maps/search/?api=1&query=いっとうや+CoCoLo新潟店")

# --- タブ2：持ち物リスト ---
with tab2:
    st.subheader("🧳 忘れ物はない？")
    for item in ["🧣 マフラー", "🧤 手袋", "🥾 滑りにくい靴", "🧥 ダウンジャケット", "🔋 モバイルバッテリー"]:
        st.checkbox(item)

# --- タブ3：予算計算 ---
with tab3:
    st.subheader("💰 お金計算")
    transport = st.number_input("交通費", value=20000)
    hotel = st.number_input("宿泊費", value=8000)
    food = st.number_input("飲食代", value=15000)
    st.metric("合計予想", f"{transport + hotel + food:,} 円")

# --- タブ4：日本酒メモ（新機能） ---
with tab4:
    st.subheader("🍶 ぽんしゅ館・利き酒メモ")
    st.write("駅ビルの「ぽんしゅ館」で気に入ったお酒をメモしておこう！")
    sake_name = st.text_input("お酒の名前")
    sake_score = st.slider("お気に入り度", 1, 5, 3)
    if st.button("メモを保存（画面上のみ）"):
        st.write(f"📝 メモしました！: **{sake_name}** (評価: {'⭐' * sake_score})")

# サイドバー
with st.sidebar:
    st.header("🌦️ 寒さ・移動対策")
    st.link_button("☀️ Yahoo!天気", "https://weather.yahoo.co.jp/weather/jp/15/5410.html")
    st.write("---")
    st.write("雪で歩けない時は無理せずタクシーを！")
    st.link_button("🚕 GO（タクシー配車）", "https://go.goinc.jp/")
    st.write("---")
    st.write("Albirex Niigata Spirit! 🦢")
