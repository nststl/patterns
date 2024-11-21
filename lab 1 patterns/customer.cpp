#include "customer.h"
#include <iostream>

void Customer::talk(int minute, Customer& other) {
    double cost = operator_->calculateTalkingCost(minute, *this);
    if (bill->check(cost)) { // Використано bill
        std::cout << name << " spoke with " << other.getName() << " for " << minute << " minutes at a cost of " << cost << " grn.\n";
    }
}

void Customer::message(int quantity, Customer& other) {
    double cost = operator_->calculateMessageCost(quantity, *this, other);
    if (bill->check(cost)) { // Використано bill
        std::cout << name << " sent " << quantity << " messages to " << other.getName() << " at a cost of " << cost << " grn.\n";
    }
}

void Customer::connectToInternet(double amount) {
    double cost = operator_->calculateNetworkCost(amount);
    if (bill->check(cost)) { // Використано bill
        std::cout << name << " connected to the internet at a cost of " << cost << " grn.\n";
    }
}

