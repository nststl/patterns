#include "Bill.h"

bool Bill::check(double amount) {
    return currentDebt + amount <= limitingAmount;
}

void Bill::add(double amount) {
    currentDebt += amount;
}

void Bill::pay(double amount) {
    currentDebt -= amount;
}

void Bill::changeLimit(double newLimit) {
    limitingAmount = newLimit;
}

double Bill::getCurrentDebt() {
    return currentDebt;
}

