import scala.util.Random
package Algebraic {

  trait AlgebraicNode {

    def evaluate(x: Int, y: Int, z: Int): Int = this match {
      case Id(s) => s match {
        case 'x => x
        case 'y => y
        case 'z => z
      }
      case Plus(n1, n2) => n1.evaluate(x, y, z) + n2.evaluate(x, y, z)
      case Minus(n1, n2) => n1.evaluate(x, y, z) - n2.evaluate(x, y, z)
      case Mult(n1, n2) => n1.evaluate(x, y, z) * n2.evaluate(x, y, z)
      // se establece que x / 0 es x
      case Div(n1, n2) =>
        if (n2.evaluate(x, y, z) == 0) n1.evaluate(x, y, z)
        else n1.evaluate(x, y, z) / n2.evaluate(x, y, z)
    }

    /*
  Ejemplo: el arbol Minus(Plus(Id('x), Id('y)), Id('z))
  imprime
  ( - )
    ( + )
        ( 'x )
        ( 'y )
    ( 'z )
   */
    def prettyPrint(ident: Int = 0): Unit = this match {
      case Plus(n1, n2) =>
        print(" " * ident)
        println("( + )")
        n1.prettyPrint(ident + 4)
        n2.prettyPrint(ident + 4)

      case Minus(n1, n2) =>
        print(" " * ident)
        println("( - )")
        n1.prettyPrint(ident + 4)
        n2.prettyPrint(ident + 4)

      case Mult(n1, n2) =>
        print(" " * ident)
        println("( * )")
        n1.prettyPrint(ident + 4)
        n2.prettyPrint(ident + 4)

      case Div(n1, n2) =>
        print(" " * ident)
        println("( / )")
        n1.prettyPrint(ident + 4)
        n2.prettyPrint(ident + 4)

      case Id(s) =>
        print(" " * ident)
        println(s"( $s )")
    }

    def randomNode: AlgebraicNode = {
      val h = this.height
      val r = Random.nextInt(h)
      this match {
        case Plus(n1, n2) =>
          if (r == 0) this
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) n1.randomNode
            else n2.randomNode
          }
        case Minus(n1, n2) =>
          if (r == 0) this
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) n1.randomNode
            else n2.randomNode
          }
        case Mult(n1, n2) =>
          if (r == 0) this
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) n1.randomNode
            else n2.randomNode
          }
        case Div(n1, n2) =>
          if (r == 0) this
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) n1.randomNode
            else n2.randomNode
          }
        case Id(s) => this
      }
    }

    def replaceRandomNodeWith(node: AlgebraicNode): AlgebraicNode = {
      val h = this.height
      val r = Random.nextInt(h)
      this match {
        case Id(s) =>
          if (r == 0) node
          else this
        case Plus(n1, n2) =>
          if (r == 0) node
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) Plus(n1.replaceRandomNodeWith(node), n2)
            else Plus(n1, n2.replaceRandomNodeWith(node))
          }
        case Minus(n1, n2) =>
          if (r == 0) node
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) Minus(n1.replaceRandomNodeWith(node), n2)
            else Minus(n1, n2.replaceRandomNodeWith(node))
          }
        case Mult(n1, n2) =>
          if (r == 0) node
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) Mult(n1.replaceRandomNodeWith(node), n2)
            else Mult(n1, n2.replaceRandomNodeWith(node))
          }
        case Div(n1, n2) =>
          if (r == 0) node
          else {
            val r2 = Random.nextInt(2)
            if (r2 == 0) Div(n1.replaceRandomNodeWith(node), n2)
            else Div(n1, n2.replaceRandomNodeWith(node))
          }
      }
    }

    def height: Int = this match {
      case Id(s) => 0
      case Plus(n1, n2) =>
        val lh = n1.height
        val rh = n2.height
        if (lh > rh) lh + 1
        else rh + 1
      case Minus(n1, n2) =>
        val lh = n1.height
        val rh = n2.height
        if (lh > rh) lh + 1
        else rh + 1
      case Mult(n1, n2) =>
        val lh = n1.height
        val rh = n2.height
        if (lh > rh) lh + 1
        else rh + 1
      case Div(n1, n2) =>
        val lh = n1.height
        val rh = n2.height
        if (lh > rh) lh + 1
        else rh + 1
    }

  }

  case class Id(s: Symbol) extends AlgebraicNode

  case class Plus(l: AlgebraicNode, r: AlgebraicNode) extends AlgebraicNode

  case class Minus(l: AlgebraicNode, r: AlgebraicNode) extends AlgebraicNode

  case class Mult(l: AlgebraicNode, r: AlgebraicNode) extends AlgebraicNode

  case class Div(l: AlgebraicNode, r: AlgebraicNode) extends AlgebraicNode

  object RandomAlgebraicTree {

    /*
    Genera un arbol con cierta profundidad.
    */
    def generate(depth: Int): AlgebraicNode = {
      if (depth == 0) Id(Random.nextInt(3) match {
        case 0 => 'x
        case 1 => 'y
        case _ => 'z
      })
      else {
        Random.nextInt(4) match {
          case 0 => Plus(generate(depth - 1), generate(depth - 1))
          case 1 => Minus(generate(depth - 1), generate(depth - 1))
          case 2 => Mult(generate(depth - 1), generate(depth - 1))
          case _ => Div(generate(depth - 1), generate(depth - 1))
          //case _ => Number(new Random().nextInt(100))
        }
      }

    }
  }

}