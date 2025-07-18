#!/usr/bin/env python3
"""
Discord Webhook受信サーバー
Discord日報をObsidianに連携するためのエンドポイント
"""

from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime
import json
import os
from pathlib import Path
import logging
from typing import Optional, List, Dict

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPIアプリケーション
app = FastAPI(title="Discord-Obsidian Sync")

# セキュリティ
security = HTTPBearer()

# 設定
CONFIG_PATH = Path(__file__).parent / "config.json"
INBOX_PATH = Path(__file__).parent.parent / "00_Inbox" / "discord"
INBOX_PATH.mkdir(parents=True, exist_ok=True)

# 設定読み込み
def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"webhook_token": "your-secret-token-here"}

config = load_config()

# データモデル
class DiscordMessage(BaseModel):
    content: str
    author: Dict[str, str]
    timestamp: str
    channel: Dict[str, str]
    attachments: Optional[List[Dict]] = []
    embeds: Optional[List[Dict]] = []

class WebhookPayload(BaseModel):
    type: str
    data: Dict

# 認証
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != config["webhook_token"]:
        raise HTTPException(status_code=403, detail="Invalid token")
    return credentials.credentials

# ルートエンドポイント
@app.get("/")
async def root():
    return {"status": "Discord-Obsidian Sync Server is running"}

# Webhook受信エンドポイント
@app.post("/webhook/discord")
async def receive_discord_webhook(
    payload: WebhookPayload,
    token: str = Depends(verify_token)
):
    """Discord Webhookを受信して処理"""
    try:
        # ペイロードタイプに応じて処理
        if payload.type == "daily_report":
            return await process_daily_report(payload.data)
        elif payload.type == "question":
            return await process_question(payload.data)
        elif payload.type == "progress":
            return await process_progress(payload.data)
        else:
            logger.warning(f"Unknown payload type: {payload.type}")
            return {"status": "ignored", "reason": "unknown payload type"}
            
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

async def process_daily_report(data: Dict):
    """日報を処理"""
    # メッセージ情報を抽出
    author = data.get("author", {}).get("username", "unknown")
    content = data.get("content", "")
    timestamp = data.get("timestamp", datetime.now().isoformat())
    
    # 日付を解析
    try:
        dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        date_str = dt.strftime("%Y-%m-%d")
    except:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    # ファイル名を生成
    filename = f"{author}_{date_str}_日報.json"
    filepath = INBOX_PATH / filename
    
    # データを保存
    report_data = {
        "type": "daily_report",
        "author": author,
        "date": date_str,
        "timestamp": timestamp,
        "content": content,
        "raw_data": data
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    
    logger.info(f"Saved daily report: {filename}")
    
    # 自動解析をトリガー（後で実装）
    # analyze_report(filepath)
    
    return {
        "status": "success",
        "message": f"Daily report saved: {filename}",
        "path": str(filepath)
    }

async def process_question(data: Dict):
    """質問を処理"""
    author = data.get("author", {}).get("username", "unknown")
    content = data.get("content", "")
    timestamp = data.get("timestamp", datetime.now().isoformat())
    
    # ファイル名を生成
    filename = f"{author}_questions.json"
    filepath = INBOX_PATH / filename
    
    # 既存の質問リストを読み込む
    questions = []
    if filepath.exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            questions = json.load(f)
    
    # 新しい質問を追加
    questions.append({
        "timestamp": timestamp,
        "content": content,
        "status": "open",
        "raw_data": data
    })
    
    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    logger.info(f"Added question for {author}")
    
    return {
        "status": "success",
        "message": f"Question saved for {author}"
    }

async def process_progress(data: Dict):
    """進捗報告を処理"""
    author = data.get("author", {}).get("username", "unknown")
    content = data.get("content", "")
    timestamp = data.get("timestamp", datetime.now().isoformat())
    
    # ファイル名を生成
    filename = f"{author}_progress.json"
    filepath = INBOX_PATH / filename
    
    # 既存の進捗リストを読み込む
    progress_list = []
    if filepath.exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            progress_list = json.load(f)
    
    # 新しい進捗を追加
    progress_list.append({
        "timestamp": timestamp,
        "content": content,
        "raw_data": data
    })
    
    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(progress_list, f, ensure_ascii=False, indent=2)
    
    logger.info(f"Added progress for {author}")
    
    return {
        "status": "success",
        "message": f"Progress saved for {author}"
    }

# サーバー起動用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)