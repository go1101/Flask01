from flask import Flask, redirect, request　#リダイレクト、リクエスト
from flask import render_template, send_file #テンプレートエンジン、
import os, json, time
import fs_data　#ファイルを管理するモジュール

