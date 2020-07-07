#!/usr/bin/env python3

import subprocess
import pyautogui
import unittest
import time
import os




def run_app():
    subprocess.call("python3 ./main.py -t 0 1000 &", shell=True)
    time.sleep(0.5)

def kill_app():
    subprocess.call("kill `ps -e --context | grep -v grep |grep ./main.py | cut -d ' ' -f1`", shell=True)



class TestExitMethods(unittest.TestCase):
    def assertExit(self):
        self.assertEqual("", subprocess.getoutput("ps -e --context | grep -v grep | grep ./main.py"))


    def test_quit_no_modify_shortcut(self):
        run_app()
        pyautogui.hotkey("ctrl", "q")
        self.assertExit()


    def test_quit_modify_shortcut(self):
        run_app()
        pyautogui.write("Hey!")
        pyautogui.hotkey("ctrl","q")
        pyautogui.moveTo(498, 688)
        pyautogui.click()
        self.assertExit()

    def test_quit_no_modify_window(self):
        run_app()
        pyautogui.moveTo(986, 194)
        pyautogui.click()
        self.assertExit()

    def test_quit_modify_window(self):
        run_app()
        pyautogui.write("Hey!")
        pyautogui.moveTo(986, 194)
        pyautogui.click()
        pyautogui.moveTo(498, 688)
        pyautogui.click()
        self.assertExit()

    def test_quit_no_modify_menu(self):
        run_app()
        pyautogui.write("Hey!")
        pyautogui.moveTo(20, 220)
        pyautogui.click()
        pyautogui.moveTo(120, 376)
        pyautogui.click()
        pyautogui.moveTo(498, 688)
        pyautogui.click()
        self.assertExit()

    def test_quit_modify_menu(self):
        run_app()
        pyautogui.moveTo(20, 220)
        pyautogui.click()
        pyautogui.moveTo(120, 376)
        pyautogui.click()
        pyautogui.moveTo(498, 688)
        pyautogui.click()
        self.assertExit()


class ManageFileTest(unittest.TestCase):
    def test_save_shortcut(self):
        run_app()
        pyautogui.write("Hey!")
        pyautogui.hotkey("ctrl", "s")
        pyautogui.write("test1")
        pyautogui.hotkey("enter")
        time.sleep(0.5)
        kill_app()

        with open("test1.txt") as f:
            in_file = f.read()

        os.remove("./test1.txt")
        self.assertEqual("Hey!", in_file)

    def test_save_menu(self):
        run_app()
        pyautogui.write("Hey! 42")
        pyautogui.moveTo(24, 214)
        pyautogui.click()
        pyautogui.moveTo(24, 314)
        pyautogui.click()
        pyautogui.write("test4")
        pyautogui.hotkey("enter")

        with open("test4.txt") as f:
            in_file = f.read()

        kill_app()
        os.remove("test4.txt")
        self.assertEqual("Hey! 42", in_file)

    def test_open_and_save_as_shortcut(self):
        subprocess.run("echo -n 42 > test2.txt", shell=True)
        run_app()
        pyautogui.hotkey("ctrl","o")
        time.sleep(0.5)
        pyautogui.write("test2.txt")
        pyautogui.hotkey("enter")
        pyautogui.hotkey("ctrl","shift","s")
        time.sleep(0.5)
        pyautogui.write("test3")
        pyautogui.hotkey("enter")
        time.sleep(0.5)
        kill_app()

        with open("test3.txt") as f:
            in_file = f.read()

        os.remove("test2.txt")
        os.remove("test3.txt")

        self.assertEqual("42", in_file)

    def test_modify_save(self):
        subprocess.run("echo -n 42 > test4.txt", shell=True)
        run_app()
        pyautogui.hotkey("ctrl","o")
        time.sleep(0.5)
        pyautogui.write("test4.txt")
        pyautogui.hotkey("enter")
        pyautogui.write("42")
        pyautogui.hotkey("ctrl","s")
        time.sleep(0.5)

        kill_app()
        with open("test4.txt") as f:
            in_file = f.read()

        os.remove("test4.txt")
        self.assertEqual("4242", in_file)




if (__name__ == "__main__"):
    unittest.main()
