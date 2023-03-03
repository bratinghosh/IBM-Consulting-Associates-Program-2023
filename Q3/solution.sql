SELECT owner_id, owner_name, COUNT(category_article_mapping.category_id) as different_category_count
FROM owner, article, category_article_mapping
WHERE article.owner_id = owner.owner_id
AND article.category_id = category_article_mapping.category_id
GROUP BY owner.owner_id
ORDER BY COUNT(category_article_mapping.category_id) DESC;