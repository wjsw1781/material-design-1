from ._anvil_designer import MyPageFormTemplate
from anvil import *
import anvil.server

class MyPageForm(MyPageFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        # 从 properties 中获取参数
        image_url = properties.get('image_url', '默认图片URL')
        title = properties.get('title', '默认标题')

        # 使用参数初始化组件

        self.button_1.text = title
