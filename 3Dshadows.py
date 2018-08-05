"""On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.
"""
class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """


        xsh = self.get_x_shadow(grid)
        ysh = self.get_y_shadow(grid)
        zsh = self.get_z_shadow(grid)

        return xsh + ysh + zsh

    def get_x_shadow(self, grid):

        shadow = 0

        for row in grid:
            for t in row:
                if t > 0:
                    shadow += 1
        return shadow

    def get_y_shadow(self, grid):

        heights = []

        for row in grid:
            tallest = 0
            for t in row:
                if t > tallest:
                    tallest = t
            heights.append(tallest)

        shadow = 0

        for h in heights:
            shadow = shadow + h

        return shadow

    def get_z_shadow(self, grid):
        shadow = 0
        heights = []

        l = len(grid)

        for i in range(l):
            heights.append(0)

        for i in range(l):
            for row in grid:
                if row[i] > heights[i]:
                    heights[i] = row[i]

        for h in heights:
            shadow = shadow + h

        return shadow
