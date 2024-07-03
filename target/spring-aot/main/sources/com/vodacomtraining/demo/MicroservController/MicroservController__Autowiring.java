package com.vodacomtraining.demo.MicroservController;

import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.aot.AutowiredFieldValueResolver;
import org.springframework.beans.factory.support.RegisteredBean;

/**
 * Autowiring for {@link MicroservController}.
 */
@Generated
public class MicroservController__Autowiring {
  /**
   * Apply the autowiring.
   */
  public static MicroservController apply(RegisteredBean registeredBean,
      MicroservController instance) {
    AutowiredFieldValueResolver.forRequiredField("microservService").resolveAndSet(registeredBean, instance);
    return instance;
  }
}
