package com.vodacomtraining.demo.MicroservService2;

import com.vodacomtraining.demo.MicroservModel.MicroservModelProduct;
import com.vodacomtraining.demo.MicroservModel.Order;
import com.vodacomtraining.demo.MicroservModel.OrderItem;
import com.vodacomtraining.demo.Repository.OrderRepository;
import com.vodacomtraining.demo.Repository.ProductRepository;
import com.vodacomtraining.demo.dto.OrderDto;
import com.vodacomtraining.demo.dto.OrderItemDto;
import jakarta.persistence.NoResultException;
import org.springframework.boot.autoconfigure.web.client.RestTemplateAutoConfiguration;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.*;

@Service
public class OrderService {

    private final OrderRepository orderRepository;
    private final ProductRepository productRepository;
    private final RestTemplate restTemplate;

    public OrderService(OrderRepository orderRepository, ProductRepository productRepository, RestTemplate restTemplate) {
        this.orderRepository = orderRepository;
        this.productRepository = productRepository;
        this.restTemplate = restTemplate;
    }

    public Map<String, String> createOrder(OrderDto orderDto) {
            // Check if user exists (assuming user service URL is "http://user-service/users/{userId}")
            String userExistsUrl = "http://user-service/users/" + orderDto.userId();
            try {
                restTemplate.getForObject(userExistsUrl, Boolean.class);
            } catch (Exception e) {
                throw new IllegalArgumentException("Invalid user ID: " + orderDto.userId());
            }
        var order = new Order();
        order.setPaymentMethod(orderDto.paymentMethod());

        double totalAMount = 0;
        var orderItems = new ArrayList<OrderItem>();

        for (OrderItemDto orderItemDto : orderDto.orderItems()) {

            Optional<MicroservModelProduct> optionalProduct = productRepository.findById(orderItemDto.productId());

            if (optionalProduct.isEmpty())
                throw new NoResultException("Product not found for the given id");

            var product = optionalProduct.get();
            var orderItem = new OrderItem();

            orderItem.setQuantity(orderItemDto.quantity());
            orderItem.setProductId((long) orderItemDto.productId());
            var orderItemTotalAmount = (double) orderItemDto.quantity() * product.getUnitPrice();
            orderItem.setTotalPrice(orderItemTotalAmount);
            orderItem.setOrder(order);
            totalAMount = totalAMount + orderItemTotalAmount;
            orderItems.add(orderItem);
        }

        order.setOrderItems(orderItems);
        order.setTotalAmount(totalAMount);
        order.setUserId((long) orderDto.userId());

        order = orderRepository.save(order);

        Map<String, String> reponse = new HashMap<>();
        reponse.put("user", "" + orderDto.userId());
        reponse.put("order-id", "" + order.getId());
        return reponse;

    }

    public Order getOrderById(Long id) {
        return orderRepository.findById(id).orElseThrow(null);
    }

    public List<Order> getAllOrders() {
        return orderRepository.findAll();
    }

    public Order updateOrder(Order order) {
        orderRepository.save(order);
        return order;
    }

    public void deleteOrder(Long id) {
        orderRepository.deleteById(id);
    }


}
