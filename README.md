# matching_pairs
コミットプラン企業と特定買手５社のマッチング済みペアの一覧

## 利用方法
- 依存関係のインストール
```bash
make install
```

## コード修正後の対応
### 新規Dockerイメージの作成＆アップロード
```bash
# ECR認証
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 849152961389.dkr.ecr.ap-northeast-1.amazonaws.com

# Dockerイメージの構築
docker build -t matching-pairs .

# イメージのタグ付け
docker tag matching-pairs:latest 849152961389.dkr.ecr.ap-northeast-1.amazonaws.com/matching-pairs:latest

# 作成したイメージをECRにプッシュ
docker push 849152961389.dkr.ecr.ap-northeast-1.amazonaws.com/matching-pairs:latest
```

### 新規イメージをデプロイ
1. AWSコンソールから「Lambda」を選択
2. 関数から「matching-pairs」を選択
3. イメージの「新しいイメージをデプロイ」を選択
4. 「イメージを参照」を選択
5. matching-pairsレポジトリのイメージタグがlatestのイメージを選択・保存
