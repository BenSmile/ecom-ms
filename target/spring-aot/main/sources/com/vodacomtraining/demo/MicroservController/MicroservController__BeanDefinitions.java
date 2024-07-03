package com.vodacomtraining.demo.MicroservController;

import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.InstanceSupplier;
import org.springframework.beans.factory.support.RootBeanDefinition;

/**
 * Bean definitions for {@link MicroservController}.
 */
@Generated
public class MicroservController__BeanDefinitions {
  /**
   * Get the bean definition for 'microservController'.
   */
  public static BeanDefinition getMicroservControllerBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(MicroservController.class);
    InstanceSupplier<MicroservController> instanceSupplier = InstanceSupplier.using(MicroservController::new);
    instanceSupplier = instanceSupplier.andThen(MicroservController__Autowiring::apply);
    beanDefinition.setInstanceSupplier(instanceSupplier);
    return beanDefinition;
  }
}
