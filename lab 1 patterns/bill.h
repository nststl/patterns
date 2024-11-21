#ifndef BILL_H
#define BILL_H

class Bill {
public:
    double limitingAmount;
    double currentDebt;

    // Конструктор
    Bill(double limit) : limitingAmount(limit), currentDebt(0) {}

    // Методи
    bool check(double amount);
    void add(double amount);
    void pay(double amount);
    void changeLimit(double newLimit);
    double getCurrentDebt();
};

#endif // BILL_H
