#ifndef OPERATOR_H
#define OPERATOR_H

class Customer; // Попереднє оголошення класу Customer

class Operator {
private:
    int id;                      // Унікальний ідентифікатор оператора
    double talkingCharge;        // Вартість за хвилину розмови
    double messageCost;          // Вартість за повідомлення
    double networkCharge;        // Вартість за використання інтернету

public:
    // Конструктор для ініціалізації
    Operator(int id, double callRate, double messageCost, double internetCost)
        : id(id), talkingCharge(callRate), messageCost(messageCost), networkCharge(internetCost) {}

    double calculateTalkingCost(int minute, Customer& customer);
    double calculateMessageCost(int quantity, Customer& customer, Customer& other);
    double calculateNetworkCost(double amount);

    int getID() const { return id; }  // Геттер для ID
};

#endif // OPERATOR_H
