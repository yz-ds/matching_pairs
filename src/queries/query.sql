SELECT
    am.id AS `マッチングID`,
    cp1.name AS `売り手企業名`,
    cp2.name AS `買い手企業名`,
    pm.name AS `プロジェクト名`,
    CASE am.matching_kind
        WHEN 0 THEN 'ターゲットマッチング'
        WHEN 1 THEN 'コロンボアライアンス'
        WHEN 2 THEN 'コラボマッチング'
        WHEN 3 THEN 'ホリゾンタルマッチング'
        WHEN 4 THEN 'ナレッジマッチング'
        WHEN 5 THEN 'ファイナンスマッチング'
        WHEN 6 THEN 'コンペマッチング'
        WHEN 7 THEN 'オープンマッチング'
        ELSE 'その他'
    END AS `マッチング種別`,
    am.meeting_date AS `商談日時`,
    CASE
        WHEN am.invalid_flag IS NOT NULL THEN '無効'
        WHEN am.matching_status = 0 THEN '進行中'
        WHEN am.matching_status = 1 THEN '完了'
        WHEN am.matching_status = 2 THEN '解消'
        ELSE 'その他'
    END AS `ステータス`
FROM
    mycsess_production.auto_matchings AS am
LEFT OUTER JOIN
    mycsess_production.companies cp1 ON am.main_company_id = cp1.id
LEFT OUTER JOIN
    mycsess_production.companies cp2 ON am.sub_company_id = cp2.id
LEFT OUTER JOIN
    mycsess_production.project_manages pm ON am.project_id = pm.id
WHERE
    cp1.master_plan_id = 60
    AND
    am.sub_company_id IN (84, 691, 991, 1000013, 1000022)
    AND
    am.deleted_at IS NULL
;
