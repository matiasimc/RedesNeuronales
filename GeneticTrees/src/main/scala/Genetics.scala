object ArithmeticGenetics {
  import Arithmetic._
  /*
  Selecciona n arboles ordenados por fitness (menor fitness, mejor)
   */
  def arithmeticSelection(ln : List[ArithmeticNode], n : Int, fitness: ArithmeticNode => Double) : List[ArithmeticNode] = {
    val sortFun = (n1 : ArithmeticNode, n2 : ArithmeticNode) => fitness(n1) < fitness(n2)
    ln.sortWith(sortFun).take(n)
  }

  /*
  Genera n hijos a partir de una lista de arboles, y muto algun hijo con probabilidad 1%
   */
  def arithmeticCrossover(ln: List[ArithmeticNode], n : Int) : List[ArithmeticNode]  = {
    import scala.util.Random
    var l : List[ArithmeticNode] = List()
    for (i <- 1 to n) {
      val parents = Random.shuffle(ln).take(2)
      val child = parents(0).replaceRandomNodeWith(parents(1).randomNode)
      val r = Random.nextInt(100)
      if (r == 0) l = arithmeticMutation(child) :: l
      else
        l = child :: l
    }
    l
  }

  /*
  Muto un arbol en particular
   */
  private def arithmeticMutation(n: ArithmeticNode) : ArithmeticNode = {
    n.replaceRandomNodeWith(RandomArithmeticTree.generate(3))
  }
}

object AlgebraicGenetics {
  import Algebraic._

  /*
  Selecciona n arboles ordenados por fitness (menor fitness, mejor)
   */
  def algebraicSelection(ln : List[AlgebraicNode], n : Int, fitness: AlgebraicNode => Double) : List[AlgebraicNode] = {
    val sortFun = (n1 : AlgebraicNode, n2 : AlgebraicNode) => fitness(n1) < fitness(n2)
    ln.sortWith(sortFun).take(n)
  }

  /*
  Genero n hijos a partir de una lista de arboles, y muto algun hijo con probabilidad 1%
   */
  def algebraicCrossover(ln: List[AlgebraicNode], n : Int) : List[AlgebraicNode]  = {
    import scala.util.Random
    var l : List[AlgebraicNode] = List()
    for (i <- 1 to n) {
      val parents = Random.shuffle(ln).take(2)
      val child = parents(0).replaceRandomNodeWith(parents(1).randomNode)
      val r = Random.nextInt(100)
      if (r == 0) l = algebraicMutation(child) :: l
      else
        l = child :: l
    }
    l
  }

  /*
  Muto un arbol en particular
   */
  private def algebraicMutation(n: AlgebraicNode) : AlgebraicNode = {
    n.replaceRandomNodeWith(RandomAlgebraicTree.generate(3))
  }
}