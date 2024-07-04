package com.vodacomtraining.demo.MicroservModel;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;

import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "orders")
public class Order {

    public Order() {
    }

    public Order(Long id, List<OrderItem> orderItems, String paymentMethod, Double totalAmount, Long userId) {
        super();
        this.id = id;
        this.orderItems = orderItems;
        this.paymentMethod = paymentMethod;
        this.totalAmount = totalAmount;
        this.userId = userId;
    }

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(name = "user_id")
    private Long userId;

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL)
    private List<OrderItem> orderItems = new ArrayList<>();

    @Column(name = "total_amount")
    private Double totalAmount;

    @Column(name = "payment_method")
    private String paymentMethod;

    // Getters, setters, and constructors (omitted for brevity)


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public List<OrderItem> getOrderItems() {
        return orderItems;
    }

    public void setOrderItems(List<OrderItem> orderItems) {
        this.orderItems = orderItems;
    }

    public String getPaymentMethod() {
        return paymentMethod;
    }

    public void setPaymentMethod(String paymentMethod) {
        this.paymentMethod = paymentMethod;
    }

    public Double getTotalAmount() {
        return totalAmount;
    }

    public void setTotalAmount(Double totalAmount) {
        this.totalAmount = totalAmount;
    }

    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public void calculateTotalAmount() {
        this.totalAmount = 0.0;
        for (OrderItem orderItem : orderItems) {
            this.totalAmount += orderItem.getTotalPrice();
        }
    }
}
