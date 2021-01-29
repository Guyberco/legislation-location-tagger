import unittest
import src.googleTrans as googleT

class TestGoogleTrans(unittest.TestCase):



    def test_checkIsLocationInTranslate(self):
        loc_texts = ["דמשק"]
        not_loc_texts = ["בית ספר","חלון","ניר" ,"שולחן"]
        # for text in loc_texts:
        #     self.assertEqual(True, googleT.checkIsLocationInTranslate(text))
        # for text in not_loc_texts:
        #     self.assertEqual(False,  googleT.checkIsLocationInTranslate(text))
        # self.assertEqual(False,  googleT.checkIsLocationInTranslate("אני כותב על ניר"))
        transT = googleT.tranlsateText("אני הולך לרחובות")
        taggedT = googleT.tagEnglishText(transT)
        print(taggedT)
        # self.assertEqual(True,  googleT.checkIsLocationInTranslate("אני הולך לקיבוץ ניר"))
        # self.assertEqual(True, googleT.checkIsLocationInTranslate("אני הולך לחולון"))






if __name__ == '__main__':
    unittest.main()