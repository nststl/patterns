#include "Operator.h"
#include "Customer.h"

double Operator::calculateTalkingCost(int minute, Customer& customer) {
    double cost = minute * talkingCharge;
    return cost;  // Для простоти, знижки можуть бути застосовані пізніше
}

double Operator::calculateMessageCost(int quantity, Customer& customer, Customer& other) {
    double cost = quantity * messageCost;
    return cost;  // Для простоти, знижки можуть бути застосовані пізніше
}

double Operator::calculateNetworkCost(double amount) {
    return amount * networkCharge;
}
