-- 1️⃣ Check the group(s) by name
SELECT id, name, category_id 
FROM res_groups 
WHERE name::text LIKE '%Commission Sale Administrator%';



-- Delete access rule records referencing this group (if safe)
DELETE FROM ir_model_data
WHERE model = 'ir.model.access'
  AND res_id IN (SELECT id FROM ir_model_access WHERE group_id = 65);

DELETE FROM ir_model_access 
WHERE group_id = 65;

--  Delete model data record for this group
DELETE FROM ir_model_data 
WHERE model = 'res.groups' 
  AND name = 'group_commission_sale_user';



-- 🧹 Delete those relations first
DELETE FROM rule_group_rel WHERE group_id = 65;


--  Finally delete the group itself
DELETE FROM res_groups 
WHERE id = 65;