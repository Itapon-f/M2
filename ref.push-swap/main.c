/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 22:45:04 by agiron-d          #+#    #+#             */
/*   Updated: 2025/12/02 03:21:47 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	ft_validate_string(char **tmp)
{
	int		i;
	long	nbr;

	i = 0;
	while (tmp[i])
	{
		if (!ft_validate_number(tmp[i]))
		{
			ft_split_free(tmp);
			ft_error();
		}
		nbr = ft_atoi(tmp[i]);
		if (nbr > 2147483647 || nbr < -2147483648)
		{
			ft_split_free(tmp);
			ft_error();
		}
		i++;
	}
}

static t_stack	*ft_is_string(char **argv, t_stack **a)
{
	char	**tmp;
	int		i;
	long	nbr;

	i = 0;
	tmp = ft_split(argv[1]);
	ft_validate_string(tmp);
	while (tmp[i])
	{
		nbr = ft_atoi(tmp[i]);
		ft_stack_add_back(a, ft_stack_add_new(&nbr));
		i++;
	}
	ft_split_free(tmp);
	return (*a);
}

static void	ft_validate_args(int argc, char **argv)
{
	int	i;

	i = 1;
	while (i < argc)
	{
		ft_atoi(argv[i]);
		i++;
	}
}

static t_stack	*ft_start(int argc, char **argv, t_stack **a)
{
	int		i;
	long	nbr;

	i = 1;
	if (argc == 2)
		*a = ft_is_string(argv, a);
	else
	{
		ft_validate_args(argc, argv);
		while (i < argc)
		{
			nbr = ft_atoi(argv[i]);
			ft_stack_add_back(a, ft_stack_add_new(&nbr));
			i++;
		}
	}
	return (*a);
}

int	main(int argc, char **argv)
{
	t_stack	*a;
	t_stack	*b;

	a = NULL;
	b = NULL;
	if (argc < 2)
		ft_error();
	else
		ft_start(argc, argv, &a);
	if (!a)
		ft_error();
	if (!a || ft_has_duplicates(a))
	{
		ft_stack_clear(&a);
		ft_error();
	}
	if (!ft_is_sorted(a))
		ft_execute_moves_start(&a, &b);
	ft_stack_clear(&a);
	return (0);
}
