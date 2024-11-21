#ifndef CUSTOMER_H
#define CUSTOMER_H

#include <string>
#include "Operator.h"
#include "Bill.h"

class Customer {
private:
    int id;
    std::string name;
    int age;
    Operator* operator_; // Змінено на operator_
    Bill* bill; // Додано для збереження інформації про рахунок

public:
    Customer(int id, const std::string& name, int age, Operator* op, Bill* bill)
        : id(id), name(name), age(age), operator_(op), bill(bill) {}

    Bill* getBill() {
        return bill;
    }

    int getAge() { return age; }
    std::string getName() { return name; }

    void talk(int minute, Customer& other);
    void message(int quantity, Customer& other);
    void connectToInternet(double amount);
};

#endif // CUSTOMER_H
