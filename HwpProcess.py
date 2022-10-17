# -*- coding: utf-8 -*-
import time
import shutil
import win32com.client as win32
import pandas as pd
import os, sys
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget


class HwpProcess(QWidget):
    def init(self):
        global df, excel, hwp
        df = pd.read_excel(os.path.join(os.getcwd(), "small_list.xlsm"))  # 엑셀로 데이터프레임 생성
        excel = df.iloc[[-1]]  # 마지막 행 데이터 가져오기
        hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")  # 한/글 열기
        hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")  # 보안모듈 적용(파일 열고닫을 때 팝업이 안나타남)

    def processOk(self):  # 보수공사승락서
        shutil.copyfile((os.path.join(os.getcwd(), "small(init).hwp")), (os.path.join(os.getcwd(), "보수공사승락서.hwp")))
        hwp.Open(os.path.join(os.getcwd(), "보수공사승락서.hwp"))  # 수정할 한/글 파일 열기

    def processChk(self):  # 준공검사조서
        shutil.copyfile((os.path.join(os.getcwd(), "small(after).hwp")), (os.path.join(os.getcwd(), "준공검사조서.hwp")))
        hwp.Open(os.path.join(os.getcwd(), "준공검사조서.hwp"))

    def process(self):
        field_list = [i for i in hwp.GetFieldList().split("\x02")]  # 한/글 안의 누름틀 목록 불러오기
        hwp.Run('SelectAll')
        hwp.Run('Copy')
        hwp.MovePos(3)  # 문서 끝으로 이동

        for i in range(len(excel) - 1):  # 엑셀파일 행갯수-1 만큼 한/글 페이지를 복사(기존에 한쪽이 있으니까)
            hwp.Run('Paste')
            hwp.MovePos(3)

        for page in range(len(excel)):  # 한/글 모든 페이지를 전부 순회하면서,
            for field in field_list:  # 모든 누름틀에 각각,
                hwp.PutFieldText(f'{field}{{{{{page}}}}}', excel[field].iloc[page])

        hwp.Save()
        # hwp.Quit()

    # def processOkdsk(self):
    #     shutil.copy((os.path.join(os.getcwd(), "보수공사승락서.hwp")), (os.path.join(os.environ["Userprofile"], "Desktop")))
    #
    # def processChkdsk(self):
    #     shutil.copy((os.path.join(os.getcwd(), "준공검사조서.hwp")), (os.path.join(os.environ["Userprofile"], "Desktop")))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = HwpProcess()
#     sys.exit(app.exec())
