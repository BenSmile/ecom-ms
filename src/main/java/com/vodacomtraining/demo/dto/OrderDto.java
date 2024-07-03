package com.vodacomtraining.demo.dto;

import java.util.List;

public record OrderDto(
        int userId,
        String paymentMethod,
        List<OrderItemDto> orderItems
) {

}
