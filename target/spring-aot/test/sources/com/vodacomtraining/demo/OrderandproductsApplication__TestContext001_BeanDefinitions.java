package com.vodacomtraining.demo;

import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.aot.BeanInstanceSupplier;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.RootBeanDefinition;
import org.springframework.context.annotation.ConfigurationClassUtils;
import org.springframework.web.client.RestTemplate;

/**
 * Bean definitions for {@link OrderandproductsApplication}.
 */
@Generated
public class OrderandproductsApplication__TestContext001_BeanDefinitions {
  /**
   * Get the bean definition for 'orderandproductsApplication'.
   */
  public static BeanDefinition getOrderandproductsApplicationBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(OrderandproductsApplication.class);
    beanDefinition.setTargetType(OrderandproductsApplication.class);
    ConfigurationClassUtils.initializeConfigurationClass(OrderandproductsApplication.class);
    beanDefinition.setInstanceSupplier(OrderandproductsApplication$$SpringCGLIB$$0::new);
    return beanDefinition;
  }

  /**
   * Get the bean instance supplier for 'restTemplate'.
   */
  private static BeanInstanceSupplier<RestTemplate> getRestTemplateInstanceSupplier() {
    return BeanInstanceSupplier.<RestTemplate>forFactoryMethod(OrderandproductsApplication.class, "restTemplate")
            .withGenerator((registeredBean) -> registeredBean.getBeanFactory().getBean(OrderandproductsApplication.class).restTemplate());
  }

  /**
   * Get the bean definition for 'restTemplate'.
   */
  public static BeanDefinition getRestTemplateBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(RestTemplate.class);
    beanDefinition.setInstanceSupplier(getRestTemplateInstanceSupplier());
    return beanDefinition;
  }
}
