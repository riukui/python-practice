monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01


# 1. get_yearly_revenue (연간 매출 계산)
def get_yearly_revenue(monthly_revenue):
  return monthly_revenue * 12


# 2. get_yearly_expenses (연간 비용 계산)
def get_yearly_expenses(monthly_expenses):
  return monthly_expenses * 12


yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses


# 3. get_tax_amount (세금 계산)
def get_tax_amount(profit):
  if profit > 100000:
    return profit * 0.25
  else:
    return profit * 0.15


tax_amount = get_tax_amount(profit)


# 4. apply_tax_credits (세액 공제 적용)
def apply_tax_credits(tax_amount, tax_credits):
  # amount to discount (할인할 금액)를 리턴
  return tax_amount * tax_credits


final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")
