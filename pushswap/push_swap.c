/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: itapon-f <itapon-f@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 19:05:55 by itapon-f          #+#    #+#             */
/*   Updated: 2025/12/29 15:29:13 by itapon-f         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

// recuerda liberar cada vez que utilizas split

static t_stack	*ft_stacka(t_stack *a, int argc, char argv)
{
	int	args;
	int	i;
	char **tmp;

	args = 0;
	i = 0;
	while (args < argc)
	{
		tmp = ft_split(argv[args], " ");
		ft
		ft_free_split(tmp);
		args++;
	}
	
	
}

int	main(int argc,char **argv)
{
	t_stack	*a;
	t_stack	*b;

	a = NULL;
	b = NULL;
	if (argc < 2)
		ft_error();
	else
		ft_stacka(a, argc, argv)
	...
}
