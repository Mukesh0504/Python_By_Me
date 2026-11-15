# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password  = input("Enter new password: ")

if len(password) < 6:
    strength = "weak"
elif len(password) <10:
    strength = "medium"
else:
    strength = "strong"

print("Your password is", strength)