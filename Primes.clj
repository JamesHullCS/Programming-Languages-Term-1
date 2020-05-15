(defn get-divisor [n] (println (range 2 (Math/sqrt n))))

(defn divides? [x n] 
(= (rem n x) 0))

(defn no-divisors? [n] 
(->> (range 2 n)(filter #(divides? % n)) empty?))

(defn is-prime? [n]
(if (= n 1) false (if (no-divisors? n) true false)))

(defn prime-seq [from to]
(println (filter is-prime? (range from (inc to)))))

(defn print-top-primes [from to]
(println (filter is-prime? (reverse (range from (inc to))))) ;Reverse
(println (apply + (filter is-prime? (reverse (range from (inc to))))))) ;Sum of list

(get-divisor 101)
(println (divides? 2 10)
(println (no-divisors? 7))
(println (is-prime? 1))
(prime-seq 50 100)
(print-top-primes 50 100)
