import streamlit as st

# ブラウザの設定（日本語化とエラー防止）
st.set_page_config(page_title="新潟1泊2日プランナー", page_icon="❄️")

# タイトル
st.title("❄️ 新潟1泊2日 満喫プラン作成")
st.write("2025/12/27(土)-28(日) の旅行をあなたに合わせてカスタマイズ！")

# 宿泊先情報
st.info("🏨 **宿泊先：ホテルリブマックス新潟駅前**\n\n新潟駅・万代口から徒歩圏内でアクセス抜群です。")

# --- 心理テスト・選択セクション ---
st.subheader("今の気分を教えてください ✨")
mood = st.radio("Q1. どんな旅にしたい？", 
                ["とにかく美味しいものを食べたい！", "冬の街並みをのんびり歩きたい", "お洒落なスポットを巡りたい"])

lunch_pref = st.selectbox("Q2. 2日目のランチは何系？", 
                         ["贅沢に日本海の海鮮！", "新潟名物タレかつorへぎそば", "落ち着いたカフェランチ"])

# --- プラン作成ボタン ---
if st.button("この気分でプランを作成！"):
    st.success("あなたにぴったりのモデルコースはこちら！")
    
    # --- 1日目夜の案内 ---
    st.subheader("🌙 1日目夜：新潟駅前の名店で乾杯")
    st.write("新潟に来たら絶対に外せない、人気の居酒屋です。年末は非常に混み合うので今すぐ予約を！")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🐟 いかの墨 新潟駅前店", "https://www.yonekura-group.jp/shop/ikanosumi/")
        st.caption("高級感ある個室と最高の海鮮。")
    with col2:
        st.link_button("🍶 五郎 万代店", "https://tabelog.com/niigata/A1501/A150101/15000444/")
        st.caption("地元民に愛される活気ある人気店。")

    # --- イルミネーション案内 ---
    st.subheader("✨ 冬の風物詩：光のページェント")
    st.markdown("""
    **【NIIGATA光のページェント】**
    - **場所：** 新潟駅南口・けやき通り（ホテルと反対側、駅を抜けてすぐ）
    - **時間：** 17:00 〜 24:10
    - **内容：** 約200本のけやきが16万球の光で包まれます。食後の散歩に最適！
    """)
    st.link_button("イベント公式サイト", "http://www.niigata-hikari.jp/")

    # --- メインコース ---
    st.divider()
    if mood == "とにかく美味しいものを食べたい！":
        st.write("**【1日目】** ぽんしゅ館で利き酒 → ピアBandaiで海鮮BBQ → 夜は予約した居酒屋へ！")
        st.write(f"**【2日目】** 古町エリアを散策 → ランチ：{lunch_pref} → 駅ビルCoCoLoでお土産探し")
    else:
        st.write("**【1日目】** 万代シテイでショッピング → 信濃川沿いの『やすらぎ堤』散歩 → 夜は居酒屋へ！")
        st.write(f"**【2日目】** 朱鷺メッセ展望室で絶景 → ランチ：{lunch_pref} → 最後にぽんしゅ館でお土産")

# --- お役立ちリンク ---
st.sidebar.header("🌡️ お役立ち情報")
st.sidebar.link_button("新潟市の天気予報 (tenki.jp)", "https://tenki.jp/forecast/4/18/47604/15100/")
st.sidebar.write("※12月末は雪の可能性があります。厚手のコート、マフラー、手袋を忘れずに！")
