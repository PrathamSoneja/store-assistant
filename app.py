import streamlit as st
from api_call import *
import base64

st.set_page_config(page_title="Product Information", page_icon=":mag:", layout="wide")
img_urls = ['https://m.media-amazon.com/images/I/81KoSSAwH2L._SL1500_.jpg',
           'https://www.memorys.in/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/0/0/003_100_4.jpg',
           'https://www.godrejinterio.com/imagestore/B2C/56101543SD00017/56101543SD00017_01_1500x1500.png',
           'https://www.godrejinterio.com/imagestore/B2C/DINCHR016/DINCHR016_01_1500x1500.png',
           'https://cdn.dxomark.com/wp-content/uploads/medias/post-47840/oneplus8Pro.jpg']
st.write('<div align="center"><h1>Product Information</h1></div>', unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    min-height: 200px;
    background-attachment: scroll;
    background-position: 300px 1800px;
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('10881763.jpg')

item_id = st.experimental_get_query_params().get("item_id")
if item_id is None or int(item_id[0]) > 105 or int(item_id[0]) < 101:
    st.error("Please provide a valid item id")
else:
    col1, col2, col3 = st.columns(3)
    url = f'https://540zfa.deta.dev/items/{item_id[0]}/'
    item_name, item_type, item_desc, price = info_call(url)
    x = int(item_id[0][2])-1
    img = img_urls[x]

    with col2:
        st.image(img, use_column_width=True, output_format='JPEG')

    st.subheader("Product Name")
    st.write(item_name)

    st.subheader("Product Category")
    st.write(item_type)

    st.subheader("Product Description")
    st.write(item_desc)

    st.subheader("Price")
    st.write(f'{price} Rs')
    st.write('')
    st.write('')
    st.subheader('Write your questions here')
    question = st.text_input('')
    clicked = st.button('Submit')

    if clicked == True and question != '':
        res = gpt_call(item_desc, question, st.secrets["openai_api_key"])
        st.write(res)
        #url_ = f'{url}{question}/'
        #res = ques_call(url_)
        #if not res.ok or float(res.json()['probability']) < 0.7:
        #    response = 'I cannot answer this question at the moment. Please contact a sales supervisor for assistance.'
        #    st.write(response)
        #else:
        #    st.subheader('Answer')
        #    st.write(res.json()['answer'])