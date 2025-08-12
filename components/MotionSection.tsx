'use client';

import { motion, useReducedMotion } from 'framer-motion';
import type { ReactNode } from 'react';

const fadeUpVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0 },
};

export default function MotionSection({ children }: { children: ReactNode }) {
  const shouldReduce = useReducedMotion();
  return (
    <motion.section
      initial="hidden"
      animate="visible"
      variants={shouldReduce ? { hidden: {}, visible: {} } : fadeUpVariants}
      transition={{ duration: 0.5 }}
    >
      {children}
    </motion.section>
  );
}
