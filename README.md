# matching_pairs
コミットプラン企業と特定買手５社のマッチング済みペアの一覧

```bash
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 849152961389.dkr.ecr.ap-northeast-1.amazonaws.com
```

```bash
docker build -t matching-pairs .
```

```bash
docker tag matching-pairs:latest 849152961389.dkr.ecr.ap-northeast-1.amazonaws.com/matching-pairs:latest
```

```bash
docker push 849152961389.dkr.ecr.ap-northeast-1.amazonaws.com/matching-pairs:latest
```
