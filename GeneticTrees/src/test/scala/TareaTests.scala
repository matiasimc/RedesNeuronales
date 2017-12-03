import org.scalatest._

/*
Primer ejemplo, se quiere encontrar un AST que satisfaga 40 < ast.evaluate() < 50
 */
class Example1 extends FlatSpec with Matchers {
  import Arithmetic._

  def is_solution(n : ArithmeticNode) : Boolean = {
    val ev = n.evaluate()
    ev > 40 && ev < 50
  }

  // generar 20 arboles random con profundidad 9
  var trees : List[ArithmeticNode] = List.range(0, 20).map((x) => RandomArithmeticTree.generate(9))

  // funcion de fitness, distancia al punto medio del intervalo
  val fitness = (n: ArithmeticNode) => Math.abs(n.evaluate() - 45.0)

  // se itera hasta encontrar una solucion
  var ite = 0
  var solution : ArithmeticNode = null
  while (solution == null) {

    ite += 1

    // selecciona 10 arboles para crossover, ordenados por mejor fitness
    val selection = ArithmeticGenetics.arithmeticSelection(trees, 10, fitness)

    //descomentar para obtener el fitness promedio de la seleccion
    //println(selection.map(n => fitness(n)).sum / trees.length)

    if (is_solution(selection(0))) {
      solution = selection(0)
    }

    // genera 20 hijos
    trees = ArithmeticGenetics.arithmeticCrossover(selection, 20)
  }

  s"In $ite iterations, found a solution x = ${solution.evaluate()} that" should "solve the equation 40 < x < 50" in {
    assert(is_solution(solution))
  }


}

/*
Segundo ejemplo, se quiere encontrar un AST(x,y,z) tal que 40 < AST(1,2,3) < 50
 */
class Example2 extends FlatSpec with Matchers {
  import Algebraic._

  def is_solution(n : AlgebraicNode) : Boolean = {
    val ev = n.evaluate(1,2,3)
    ev > 40 && ev < 50
  }

  // generar 20 arboles random con profundidad 9
  var trees : List[AlgebraicNode] = List.range(0,20).map((x) => RandomAlgebraicTree.generate(9))

  // funcion de fitness, distancia al punto medio del intervalo
  val fitness = (n: AlgebraicNode) => Math.abs(n.evaluate(1,2,3) - 45.0)

  // se itera hasta encontrar una solucion
  var ite = 0
  var solution : AlgebraicNode = null
  while (solution == null) {

    ite += 1

    // selecciona 10 arboles para crossover, ordenados por mejor fitness
    val selection = AlgebraicGenetics.algebraicSelection(trees, 10, fitness)

    //descomentar para obtener el fitness promedio de la seleccion
    //println(selection.map(n => fitness(n)).sum / trees.length)

    if (is_solution(selection(0))) {
      solution = selection(0)
    }

    // genera 20 hijos
    trees = AlgebraicGenetics.algebraicCrossover(selection, 20)
  }

  s"In $ite iterations, found a solution x = ${solution.evaluate(1,2,3)} that" should "solve the equation 40 < x < 50" in {
    assert(is_solution(solution))
  }


}